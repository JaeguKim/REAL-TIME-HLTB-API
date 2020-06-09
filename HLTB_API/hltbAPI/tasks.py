from time import sleep
import json
from celery import shared_task
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
from urllib import parse
from .models import Currency
 
baseURL = 'https://howlongtobeat.com'
searchSuffix = 'search_results.php'

def getSearchResult(name):
    body = {
          'queryString': name,
          't': 'games',
          'sorthead': 'popular',
          'sortd': 'Normal Order',
          'plat': '',
          'length_type': 'main',
          'length_min': '',
          'length_max': '',
          'detail': '0'
        }

    data = parse.urlencode(body).encode("utf-8")
    print(data)
    req = Request('{}/{}'.format(baseURL,searchSuffix),headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req,data=data) as f:
        resp = f.read()
        print(resp)

print(getSearchResult('Halo'))

# @shared_task
# # some heavy stuff here
# def create_currency():
#     print('Creating forex data ..')
#     req = Request('https://www.investing.com/currencies/single-currency-crosses', headers={'User-Agent': 'Mozilla/5.0'})
#     html = urlopen(req).read()
#     bs = BeautifulSoup(html, 'html.parser')
#     # get first 5 rows
#     currencies = bs.find("tbody").find_all("tr")[0:5]
#     # enumerate rows to include index inside class name
#     # starting index from 1
#     for idx, currency in enumerate(currencies, 1):
#         pair = currency.find("td", class_="plusIconTd").a.text
#         bid = currency.find("td", class_=f"pid-{idx}-bid").text
#         ask = currency.find("td", class_=f"pid-{idx}-ask").text
#         high = currency.find("td", class_=f"pid-{idx}-high").text
#         low = currency.find("td", class_=f"pid-{idx}-low").text
#         change = currency.find("td", class_=f"pid-{idx}-pc").text
#         change_p = currency.find("td", class_=f"pid-{idx}-pc").text
#         time = currency.find("td", class_=f"pid-{idx}-time").text
 
#         print({'pair':pair, 'bid':bid, 'ask':ask, 'high':high, 'low':low, 'change':change, 'change_p':change_p, 'time':time})
 
#         # create objects in database
#         Currency.objects.create(
#             pair=pair,
#             bid=bid,
#             ask=ask,
#             high=high,
#             low=low,
#             change=change,
#             change_p=change_p,
#             time=time
#         )
        
#         # sleep few seconds to avoid database block
#         sleep(5)
 
# @shared_task
# # some heavy stuff here
# def update_currency():
#     print('Updating forex data ..')
#     req = Request('https://www.investing.com/currencies/single-currency-crosses', headers={'User-Agent': 'Mozilla/5.0'})
#     html = urlopen(req).read()
#     bs = BeautifulSoup(html, 'html.parser')
#     currencies = bs.find("tbody").find_all("tr")[0:5]
#     for idx, currency in enumerate(currencies, 1):
#         pair = currency.find("td", class_="plusIconTd").a.text
#         bid = currency.find("td", class_=f"pid-{idx}-bid").text
#         ask = currency.find("td", class_=f"pid-{idx}-ask").text
#         high = currency.find("td", class_=f"pid-{idx}-high").text
#         low = currency.find("td", class_=f"pid-{idx}-low").text
#         change = currency.find("td", class_=f"pid-{idx}-pc").text
#         change_p = currency.find("td", class_=f"pid-{idx}-pc").text
#         time = currency.find("td", class_=f"pid-{idx}-time").text
 
#         # create dictionary
#         data = {'pair':pair, 'bid':bid, 'ask':ask, 'high':high, 'low':low, 'change':change, 'change_p':change_p, 'time':time}
#         # find the object by filtering and update all fields
#         Currency.objects.filter(pair=pair).update(**data)
 
#         sleep(5)


