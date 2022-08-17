from selenium import webdriver
from bs4 import BeautifulSoup
import time


def connecting(page, number_group = ''):
    url = f'{page}{number_group}'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    page = driver.page_source
    # with open("index.html", encoding='utf-8', mode="w") as file:
    #     file.write(page)
    soup = BeautifulSoup(page, 'lxml')
    print("connection successful")
    return soup


def parsing_data(soup):
    block = soup.find_all("div", {"class": "jx6 x6j"})
    list = []
    for i in range(len(block)):
        title = block[i].find("span", {"class": "dr dr0 r0d rd2 tsBodyL vj9"})
        text = title.text
        text = text.strip()
        span_price = block[i].find("span", {"ui-o9 ui-o5"})
        if span_price == None:
            span_price = ' 0'
        elif not isinstance(span_price, str):
            span_price = span_price.text.strip()
        span_price_with_discount = block[i].find("span", {"class": "ui-o1 ui-o5 ui-o8"})
        if span_price_with_discount == None:
            span_price_with_discount = ' 0'
        elif not isinstance(span_price_with_discount, str):
            span_price_with_discount = span_price_with_discount.text.strip()
        text += ' ' + span_price + ' ' + span_price_with_discount
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
    pages = ['https://www.ozon.ru/category/sredstva-dlya-stirki-14580/?category_was_predicted=true&deny_category_prediction=true&from_global=true&isbest=t',
             'https://www.ozon.ru/category/chistyashchie-sredstva-14587/?category_was_predicted=true&deny_category_prediction=true&from_global=true&isbest=t',
             'https://www.ozon.ru/category/sredstva-dlya-mytya-posudy-14591/?rating=t',
             'https://www.ozon.ru/category/osvezhiteli-vozduha-14576/?category_was_predicted=true&deny_category_prediction=true&from_global=true&isbest=t',
             'https://www.ozon.ru/search/?from_global=true&text=%D0%A1%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%BE%20%D0%B4%D0%BB%D1%8F%20%D1%83%D1%85%D0%BE%D0%B4%D0%B0%20%D0%B7%D0%B0%20%D0%B1%D1%8B%D1%82%D0%BE%D0%B2%D0%BE%D0%B9%20%D1%82%D0%B5%D1%85%D0%BD%D0%B8%D0%BA%D0%BE%D0%B9&isbest=t',
             'https://www.ozon.ru/search/?text=%D0%BC%D1%8B%D0%BB%D0%BE&from_global=true&isbest=t']
    pages_name = ['Средства для стирки OZON', 'Средства для уборки OZON', 'Средства для мытья посуды OZON', 'Освежители воздуха OZON', 'Средства для ухода за бытовой техникой OZON', 'Мыло OZON']
    for first_page in range(len(pages)):
        soup = connecting(pages[first_page], (f'&page={first_page}'))
        list = parsing_data(soup)
        saving_data_mode_w(pages_name[first_page], list)
        for number_page in range(2, 7):
            soup = connecting(pages[first_page], (f'&page={number_page}'))
            list = parsing_data(soup)
            saving_data_mode_a(pages_name[first_page], list)


if __name__ == '__main__':
    Parser()