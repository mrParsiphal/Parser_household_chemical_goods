from selenium import webdriver
from bs4 import BeautifulSoup

def connecting(page, number_group = ''):
    url = f'{page}{number_group}'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    page = driver.page_source
    # with open("index.html", encoding='utf-8', mode="w") as file:
    #     file.write(page)
    soup = BeautifulSoup(page, 'lxml')
    print("connection successful")
    return soup


def parsing_data(soup):
    blocks = soup.find("div", {"class": "subcategory-or-type__content"})
    block = blocks.find_all("div", {"class": "base-product-item__content"})
    list = []
    for i in range(len(block)):
        title = block[i].find("a", {"class": "base-product-name reset-link"})
        if title != None:
            text = title.text.strip()
            span_price = block[i].find("span", {"base-product-prices__old-sum"})
            span_price_with_discount = block[i].find("span", {"class": "base-product-prices__actual-sum"})
            if span_price == None:
                if span_price_with_discount == None:
                    text += ' 0 0'
                else:
                    span_price_with_discount = span_price_with_discount.text.strip()
                    text += ' ' + span_price_with_discount + ' 0'
            else:
                span_price = span_price.text.strip()
                if span_price_with_discount == None:
                    text += ' ' + span_price + ' 0'
                else:
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
    pages = ['https://online.metro-cc.ru/category/bytovaya-himiya/chistyaschie-sredstva',
             'https://online.metro-cc.ru/category/bytovaya-himiya/sredstva-dlya-stirki',
             'https://online.metro-cc.ru/category/bytovaya-himiya/sredstva-dlya-mytya-posudy',
             'https://online.metro-cc.ru/category/bytovaya-himiya/osvezhiteli-vozduha']
    pages_name = ['Средства для уборки METRO', 'Средства для стирки METRO', 'Средства для мытья посуды METRO', 'Освежители воздуха METRO']
    for first_page in range(len(pages)):
        soup = connecting(pages[first_page])
        list = parsing_data(soup)
        saving_data_mode_w(pages_name[first_page], list)
        quantity_pages = soup.find("ul", {"class": "catalog-paginate v-pagination"})
        quantity_pages = quantity_pages.find_all("li")
        quantity_pages = int(quantity_pages[-2].text.strip())
        for number_page in range(2, quantity_pages + 1):
            soup = connecting(pages[first_page], (f'?page={number_page}'))
            list = parsing_data(soup)
            saving_data_mode_a(pages_name[first_page], list)


if __name__ == '__main__':
    Parser()