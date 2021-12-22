import logging
import sys
import random
import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import time
start_time = time.time()



asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def send_sync_request_with_timeouts(url):
    loop = asyncio.get_event_loop()
    html = loop.run_until_complete(request_sender(url, 2))[0]
    tries = 0
    while not html and tries <= 5:
        tries += 1
        timeout = random.random() * tries * 2
        html = loop.run_until_complete(request_sender(url, timeout))[0]
    return html

async def request_sender(url, timeout):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=timeout)) as response:
                html=await response.text()
                return html, url
        except asyncio.TimeoutError as e:
            return None, url


async def get_urls(*url_list):
    final_result_list = []
    failed_list = []
    for i in range(1, 6):
        if i == 1:
            result_list = await asyncio.gather(*(request_sender(url, random.random() * i * 3) for url in url_list))
            succeed_list = list(filter(lambda result: result[0] != None, result_list))
            final_result_list += succeed_list
            failed_list = list(filter(lambda result: result[0] == None, result_list))
        elif failed_list:
            result_list = await asyncio.gather(
                *(request_sender(result[1], random.random() * i * 3) for result in failed_list))
            succeed_list = list(filter(lambda result: result[0] != None, result_list))
            final_result_list += succeed_list
           failed_list = list(filter(lambda result: result[0] == None, result_list))
    return final_result_list + failed_list



def get_current_rate(valute):
    xmldata = send_sync_request_with_timeouts(r'https://www.cbr.ru/scripts/XML_daily.asp?')
    print(xmldata)
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
    url_companies_list=[]
    for tr_tag in tr_tags:
        td_tag = tr_tag.find("td", {"class": "table__td table__td--big"})
        if td_tag:
            comp_dict = {}
            namea = td_tag.find("a")
            comp_dict['name'] = namea.text
            last_price = float(td_tag.findNext('td').contents[0].strip().replace(',', ''))
            change_per_year = float(
                td_tag.findNext('td').findNext('td').findNext('td').findNext('td').findNext('td').findNext(
                    'td').findNext(
                    'td').find("span").findNext('span').text.strip("%"))
            comp_dict['growth'] = change_per_year
            last_price_rub = round(last_price * curr_usd_rate, 2)
            comp_dict['price'] = last_price_rub
            url_companies_list.append(r'https://markets.businessinsider.com/{}'.format(namea['href']))
            one_page[r'https://markets.businessinsider.com/{}'.format(namea['href'])]=comp_dict
    result_list = asyncio.run(get_urls(*url_companies_list))
    if not list(filter(lambda result: result[0] == None, result_list)):
        for i,result in enumerate(result_list):
            one_page[result[1]]['P/E'],one_page[result[1]]['potential profit'],one_page[result[1]]['tiker']=parse_company_page(result[0])
            #one_page[i]['P/E'], one_page[i]['potential profit'], one_page[i]['tiker'] = parse_company_page(result[0])
        return list(one_page.values())
    else:
        raise ValueError

def SP500_parser():
    url_list = []
    usd_rate=74 # get_current_rate('USD') # need to redo to sync version
    for page in range(
            12):
        url = r'https://markets.businessinsider.com/index/components/s&p_500?p={}'.format(page)
        url_list.append(url)
    final_result_list=[]
    result_list = asyncio.run(get_urls(*url_list))
    for result in result_list:
        final_result_list+=parse_one_page_circle(result[0], usd_rate)
    return final_result_list


result_list = SP500_parser()
print(result_list)
print(len(result_list))

"""
Топ 10 компаний с самими дорогими акциями в рублях.
Топ 10 компаний с самым низким показателем P/E.
Топ 10 компаний, которые показали самый высокий рост за последний год
Топ 10 комппаний, которые принесли бы наибольшую прибыль, если бы были куплены на самом минимуме и проданы на самом максимуме за последний год.
"""

top_highest_price = sorted(result_list, key=lambda d: d['price'])
with open('top_highest_price.json', 'w') as file:
    json.dump(top_highest_price[-10:], file)
top_lowest_pe = sorted(result_list, key=lambda d: d['P/E'])
with open('top_lowest_pe.json', 'w') as file:
    json.dump(top_lowest_pe[-10:], file)
top_with_max_growth = sorted(result_list, key=lambda d: d['growth'])
with open('top_with_max_growth.json', 'w') as file:
    json.dump(top_with_max_growth[-10:], file)
top_highest_potential_profit = sorted(result_list, key=lambda d: d['potential profit'])
with open('top_highest_potential_profit.json', 'w') as file:
    json.dump(top_highest_potential_profit[-10:], file)


print("--- %s seconds ---" % (time.time() - start_time))