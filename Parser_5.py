import requests
import json


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


def Parser():
    urls = [['https://5ka.ru/api/v2/special_offers/?records_per_page=15&page=1&store=S801&ordering=&price_promo__gte=&price_promo__lte=&categories=573&search=', 'https://5ka.ru/api/v2/special_offers/?records_per_page=15&page=2&store=S801&ordering=&price_promo__gte=&price_promo__lte=&categories=573&search='],
            'https://5ka.ru/api/v2/special_offers/?records_per_page=15&page=1&store=S801&ordering=&price_promo__gte=&price_promo__lte=&categories=568&search=',
            'https://5ka.ru/api/v2/special_offers/?records_per_page=15&page=1&store=S801&ordering=&price_promo__gte=&price_promo__lte=&categories=574&search=',
            'https://5ka.ru/api/v2/special_offers/?records_per_page=15&page=1&store=S801&ordering=&price_promo__gte=&price_promo__lte=&categories=559&search',
            'https://5ka.ru/api/v2/special_offers/?records_per_page=15&page=1&store=S801&ordering=&price_promo__gte=&price_promo__lte=&categories=551&search=',
            'https://5ka.ru/api/v2/special_offers/?records_per_page=15&page=1&store=S801&ordering=&price_promo__gte=&price_promo__lte=&categories=571&search=',
            'https://5ka.ru/api/v2/special_offers/?records_per_page=15&page=1&store=S801&ordering=&price_promo__gte=&price_promo__lte=&categories=570&search=',
            ]
    name_pages = ['Средства для стирки 5', 'Средства для мытья посуды 5', 'Средства для чистки унитаза 5', 'Пятновыводители 5', 'Чистящие средства 5', 'Средства для чистки труб 5', 'Жироудалители 5']
    for t in range(len(urls)):
        patch = urls[t]
        if isinstance(patch, list):
            response = requests.get(urls[t][0])
            text = response.text
            massif = Decrypting(text)
            with open(f"{name_pages[t]}", encoding='utf-8', mode="w") as file:
                for i in massif:
                    file.write(i + '\n')
            for y in range(1, len(urls[t])):
                response = requests.get(urls[t][y])
                text = response.text
                massif = Decrypting(text)
                with open(f"{name_pages[t]}.txt", encoding='utf-8', mode="a") as file:
                    for i in massif:
                        file.write(i + '\n')
        else:
            response = requests.get(urls[t])
            text = response.text
            massif = Decrypting(text)
            with open(f"{name_pages[t]}.txt", encoding='utf-8', mode="w") as file:
                for i in massif:
                    file.write(i + '\n')


if __name__ == '__main__':
    Parser()