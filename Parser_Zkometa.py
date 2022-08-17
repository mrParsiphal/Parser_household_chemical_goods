import requests
from bs4 import BeautifulSoup
import time


def connecting(page, number_group = ''):
    url = f'{page}{number_group}'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    page = response.text
    soup = BeautifulSoup(page, 'lxml')
    print("connection successful")
    return soup


def parsing_data(soup):
    block = soup.find_all("div", {"class": "productItem"})
    list = []
    for i in range(len(block)):
        title = block[i].find("h3")
        text = title.text
        span_price_with_discount = block[i].find("div", {"salePrice"})
        span_price = block[i].find("div", {"class": "newPrice"})
        if span_price_with_discount != None:
            span_price_with_discount = span_price_with_discount.text.strip()
            span_price_with_discount = span_price_with_discount[:-2]
            text += ' ' + span_price_with_discount
            if span_price != None:
                span_price = span_price.text.strip()
                span_price = span_price[:-2]
                text += ' ' + span_price
            else:
                text += ' 0'
        else:
            if span_price != None:
                span_price = span_price.text.strip()
                span_price = span_price[:-2]
                text += ' ' + span_price
            else:
                text += ' 0'
            text += ' 0'
        print(text)
        list.append(text)
    return list


def saving_data_mode_a(pages_name, list):
    with open(f'{pages_name}.txt', encoding='utf-8', mode='a') as result:
        for i in list:
            result.write(i + '\n')


def saving_data_mode_w(pages_name, list):
    with open(f'{pages_name}.txt', encoding='utf-8', mode='w') as result:
        for i in list:
            result.write(i + '\n')


def Parser():
    pages = ['http://zkometa.ru/sale/26/',
             'http://zkometa.ru/sale/75/',
             'http://zkometa.ru/sale/82/',
             'http://zkometa.ru/sale/34/',
             'http://zkometa.ru/sale/83/',
             'http://zkometa.ru/sale/84/']
    pages_name = ['Средства для стирки ZCOMETA', 'Средства для уборки ZCOMETA', 'Средства для мытья посуды ZCOMETA', 'Освежители воздуха ZCOMETA', 'Средства для туалета ZCOMETA', 'Средства для мытья ванных комнат ZCOMETA']
    for j in range(len(pages)):
        soup = connecting(pages[j])
        try:
            quantity_pages = soup.find("div", {"class": "pagination"})
            quantity_pages = quantity_pages.find_all("a")
            address_page = '?PAGEN_1='
            quantity_pages = len(quantity_pages)
            print('страницы есть')
            list = parsing_data(soup)
            saving_data_mode_w(pages_name[j], list)
            for f in range(1, quantity_pages):
                soup = connecting(pages[j], address_page + str(f + 1))
                list = parsing_data(soup)
                saving_data_mode_a(pages_name[j], list)
                time.sleep(1)
        except:
            print('страниц нет')
            list = parsing_data(soup)
            saving_data_mode_w(pages_name[j], list)
            time.sleep(1)


if __name__ == '__main__':
    Parser()
