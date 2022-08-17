import requests
import gzip
import shutil
import json
from bs4 import BeautifulSoup


# response = requests.get('https://5ka.ru/api/v2/special_offers/?records_per_page=15&page=1&store=S801&ordering=&price_promo__gte=&price_promo__lte=&categories=574&search=')
# # https://5ka.ru/api/v2/special_offers/?records_per_page=15&page=2&store=S801&ordering=&price_promo__gte=&price_promo__lte=&categories=542&search=
# page = response.text
# # https://5ka.ru/api/v2/special_offers/?records_per_page=15&page=3&store=S801&ordering=&price_promo__gte=&price_promo__lte=&categories=542&search=
# with open("index.html", encoding='utf-8', mode="w") as file:
#     file.write(page)


def Decrypting(text):
    dictData = json.loads(text)
    results = dictData["results"]
    massif = []
    for i in range(len(results)):
        price = results[i].get('current_prices')
        data = str(results[i].get('name')) + ' ' + str(price.get('price_reg__min')) + ' ' + str(price.get('price_promo__min'))
        print(data)
        massif.append(data)
    return massif


def Connecting(number_group = ''):
    response = requests.get('https://sbermarket.ru/api/stores/5386/products?tid=bitovaya-himiya-uborka-%2Fsredstva-dlya-stirki&page=2&per_page=20&sort=popularity')
    dictData = json.loads(response.text)
    with open("index.html", encoding='utf-8', mode="w") as file:
        file.write(dictData)
    response = Decrypting(response)
    print("connection successful")
    print(response)

if __name__ == '__main__':
    Connecting()