import logging
import random
import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import time
from concurrent.futures import ThreadPoolExecutor

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class Parser_sp500:
    """
    This class parses sp500 index data and store it inside self.parsed_data property.
    four self.methods allow to filter data base on predefined conditions.
    """
    def __init__(self):
        """
        Init method starts parse circle
        """
        url_list = []
        usd_rate = Parser_sp500.get_current_rate("USD")
        for page in range(12):
            url = r'https://markets.businessinsider.com/index/components/s&p_500?p={}'.format(page)
            url_list.append(url)
        res_list = asyncio.run(Parser_sp500.get_urls(*url_list))

        def parse_one_page_circle_with_rate(rsult):
            return self.parse_one_page_circle(rsult[0], usd_rate)

        with ThreadPoolExecutor(max_workers=2) as pool:
            final_res_list = pool.map(parse_one_page_circle_with_rate, res_list)
        self.parsed_data = [item for sublist in list(final_res_list) for item in sublist]

    @staticmethod
    async def request_sender(url, timeout):
        """
        async function for sending requests with aiohttp library
        :param url:
        :param timeout:
        :return: tuple with text of response and url of request
        """
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as response:
                    text = await response.text()
                    return text, url
            except asyncio.TimeoutError as e:
                return None, url

    @staticmethod
    async def get_urls(*url_list):
        """
        This method handles async requests, filter failed responses,
        and send failed again with increased random timeout.
        :param url_list:
        :return: list with tuples consists of text response data and url of request
        """
        final_res_list = []
        failed_list = []
        for i in range(1, 8):
            if i == 1:
                res_list = await asyncio.gather(
                    *(Parser_sp500.request_sender(url, random.random() * i * 10) for url in url_list))
                succeed_list = list(filter(lambda rsult: rsult[0] is not None, res_list))
                final_res_list += succeed_list
                failed_list = list(filter(lambda rsult: rsult[0] is None, res_list))
            elif failed_list:
                res_list = await asyncio.gather(
                    *(Parser_sp500.request_sender(rsult[1], random.random() * i * 15) for rsult in failed_list))
                succeed_list = list(filter(lambda rsult: rsult[0] is not None, res_list))
                final_res_list += succeed_list
                failed_list = list(filter(lambda rsult: rsult[0] is None, res_list))
        return final_res_list + failed_list

    @staticmethod
    def get_current_rate(valute):
        """
        This method return current rate of specified valute from cbr.ru
        :param valute:
        :return: float value of current rate
        """
        xmldata = asyncio.run(Parser_sp500.get_urls(r'https://www.cbr.ru/scripts/XML_daily.asp?'))[0][0]
        xml = ET.fromstring(xmldata)
        for curr in xml:
            dict = {item.tag: item.text for item in curr}
            if dict['CharCode'] == valute:
                current_rate = float(dict['Value'].replace(',', '.'))
        return current_rate

    @staticmethod
    def parse_company_page(company_html):
        """
        This method handles parsing of company page
        :param company_html:
        :return: tuple with values
        """
        soup_company = BeautifulSoup(company_html, 'html.parser')
        try:
            p_e_ratio = float(
                soup_company.find("div", string='P/E Ratio').parent.contents[0].text.strip().replace(',', ''))
        except AttributeError:
            p_e_ratio = 0
        try:
            low = float(
                soup_company.find("div", string='52 Week Low').parent.contents[0].text.strip().replace(',', ''))
            high = float(
                soup_company.find("div", string='52 Week High').parent.contents[0].text.strip().replace(',', ''))
            potential_growth = round((high - low) / low * 100, 2)
        except AttributeError:
            potential_growth = 0
        tiker = soup_company.find("span", {"class": "price-section__category"}).contents[1].text.strip(
            ',').strip()
        return p_e_ratio, potential_growth, tiker

    @staticmethod
    def parse_one_page_circle(html, curr_usd_rate):
        """
        This method handles parsing of one page of index at web site.
        :param html:
        :param curr_usd_rate:
        :return:
        """
        soup = BeautifulSoup(html, 'html.parser')
        tr_tags = soup.find_all("tr")
        one_page = {}
        url_companies_list = []
        for tr_tag in tr_tags:
            td_tag = tr_tag.find("td", {"class": "table__td table__td--big"})
            if td_tag:
                """
                specified class proofs that we found a line with one company and can start parse it's values
                """
                comp_dict = {}
                a_tag = td_tag.find("a")
                comp_dict['name'] = a_tag.text
                last_price = float(td_tag.findNext('td').contents[0].strip().replace(',', ''))
                change_per_year = float(
                    td_tag.findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext(
                        'td').findNext(
                        'td').find("span").findNext('span').text.strip("%"))
                comp_dict['growth'] = change_per_year
                last_price_rub = round(last_price * curr_usd_rate, 2)
                comp_dict['price'] = last_price_rub
                url_companies_list.append(r'https://markets.businessinsider.com/{}'.format(a_tag['href']))
                one_page[r'https://markets.businessinsider.com/{}'.format(a_tag['href'])] = comp_dict
        res_list = asyncio.run(Parser_sp500.get_urls(*url_companies_list))
        if not list(filter(lambda rsult: rsult[0] is None, res_list)):
            for i, rsult in enumerate(res_list):
                one_page[rsult[1]]['P/E'], one_page[rsult[1]]['potential profit'], one_page[rsult[1]][
                    'tiker'] = Parser_sp500.parse_company_page(rsult[0])

            return list(one_page.values())
        else:
            raise ValueError

    def top_highest_price(self):
        return {'data':sorted(self.parsed_data, key=lambda d: d['price'])[-10:]}

    def top_lowest_pe(self):
        return {'data':sorted(self.parsed_data, key=lambda d: d['P/E'])[:10]}

    def top_with_max_growth(self):
        return {'data':sorted(self.parsed_data, key=lambda d: d['growth'])[-10:]}

    def top_highest_potential_profit(self):
        return {'data':sorted(self.parsed_data, key=lambda d: d['potential profit'])[-10:]}


if __name__ == '__main__':
    start_time = time.time()
    parser = Parser_sp500()
    with open('top_highest_price.json', 'w') as file:
        json.dump(parser.top_highest_price, file)
    with open('top_lowest_pe.json', 'w') as file:
        json.dump(parser.top_lowest_pe, file)
    with open('top_with_max_growth.json', 'w') as file:
        json.dump(parser.top_with_max_growth, file)
    with open('top_highest_potential_profit.json', 'w') as file:
        json.dump(parser.top_highest_potential_profit, file)

    logging.info("--- %s seconds ---" % (time.time() - start_time))
