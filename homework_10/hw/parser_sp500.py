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


async def request_sender(url, timeout):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as response:
                html = await response.text()
                return html, url
        except asyncio.TimeoutError as e:
            return None, url


async def get_urls(*url_list):
    final_res_list = []
    failed_list = []
    for i in range(1, 8):
        if i == 1:
            res_list = await asyncio.gather(*(request_sender(url, random.random() * i * 10) for url in url_list))
            succeed_list = list(filter(lambda rsult: rsult[0] is not None, res_list))
            final_res_list += succeed_list
            failed_list = list(filter(lambda rsult: rsult[0] is None, res_list))
        elif failed_list:
            res_list = await asyncio.gather(
                *(request_sender(rsult[1], random.random() * i * 15) for rsult in failed_list))
            succeed_list = list(filter(lambda rsult: rsult[0] is not None, res_list))
            final_res_list += succeed_list
            failed_list = list(filter(lambda rsult: rsult[0] is None, res_list))
    return final_res_list + failed_list


def get_current_rate(valute):
    xmldata = asyncio.run(get_urls(r'https://www.cbr.ru/scripts/XML_daily.asp?'))[0][0]
    xml = ET.fromstring(xmldata)
    for curr in xml:
        dict = {item.tag: item.text for item in curr}
        if dict['CharCode'] == valute:
            current_rate = float(dict['Value'].replace(',', '.'))
    return current_rate


def parse_company_page(company_html):
    soup_company = BeautifulSoup(company_html, 'html.parser')
    try:
        p_e_ratio = float(soup_company.find("div", string='P/E Ratio').parent.contents[0].text.strip().replace(',', ''))
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


def parse_one_page_circle(html, curr_usd_rate):
    soup = BeautifulSoup(html, 'html.parser')
    tr_tags = soup.find_all("tr")
    one_page = {}
    url_companies_list = []
    for tr_tag in tr_tags:
        td_tag = tr_tag.find("td", {"class": "table__td table__td--big"})
        if td_tag:
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
    res_list = asyncio.run(get_urls(*url_companies_list))
    if not list(filter(lambda rsult: rsult[0] is None, res_list)):
        for i, rsult in enumerate(res_list):
            one_page[rsult[1]]['P/E'], one_page[rsult[1]]['potential profit'], one_page[rsult[1]][
                'tiker'] = parse_company_page(rsult[0])

        return list(one_page.values())
    else:
        raise ValueError


def SP500_parser():
    url_list = []
    usd_rate = get_current_rate("USD")
    for page in range(12):
        url = r'https://markets.businessinsider.com/index/components/s&p_500?p={}'.format(page)
        url_list.append(url)
    res_list = asyncio.run(get_urls(*url_list))

    def parse_one_page_circle_with_rate(rsult):
        return parse_one_page_circle(rsult[0], usd_rate)

    with ThreadPoolExecutor(max_workers=2) as pool:
        final_res_list = pool.map(parse_one_page_circle_with_rate, res_list)
    flat_list = [item for sublist in list(final_res_list) for item in sublist]
    return flat_list


if __name__ == '__main__':
    start_time = time.time()

    res_list = SP500_parser()
    top_highest_price = sorted(res_list, key=lambda d: d['price'])
    with open('top_highest_price.json', 'w') as file:
        json.dump(top_highest_price[-10:], file)
    top_lowest_pe = sorted(res_list, key=lambda d: d['P/E'])
    with open('top_lowest_pe.json', 'w') as file:
        json.dump(top_lowest_pe[:10], file)
    top_with_max_growth = sorted(res_list, key=lambda d: d['growth'])
    with open('top_with_max_growth.json', 'w') as file:
        json.dump(top_with_max_growth[-10:], file)
    top_highest_potential_profit = sorted(res_list, key=lambda d: d['potential profit'])
    with open('top_highest_potential_profit.json', 'w') as file:
        json.dump(top_highest_potential_profit[-10:], file)

    logging.info("--- %s seconds ---" % (time.time() - start_time))


