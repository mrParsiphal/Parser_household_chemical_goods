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
    block = soup.find_all("div", {"class": "ProductCard_styles_root__uKQJb Product_styles_root__32vi_"})
    list = []
    for i in range(len(block)):
        title = block[i].find("a", {"class": "base-product-name reset-link"})
        if title != None:
            text = title.text.strip()
            span_price = block[i].find("span", {"base-product-prices__old-sum"})
            if span_price == None:
                span_price = ''
            elif not isinstance(span_price, str):
                span_price = span_price.text.strip()
            span_price_with_discount = block[i].find("span", {"class": "base-product-prices__actual-sum"})
            if span_price_with_discount == None:
                span_price_with_discount = ''
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
    pages = ['https://sbermarket.ru/victoria/c/bitovaya-himiya-uborka-/sredstva-dlya-stirki',
             'https://sbermarket.ru/victoria/c/bitovaya-himiya-uborka-/otbelivateli-pyatnovivoditeli',
             'https://sbermarket.ru/victoria/c/bitovaya-himiya-uborka-/konditsioneri-opolaskivateli',
             'https://sbermarket.ru/victoria/c/bitovaya-himiya-uborka-/sredstva-dlya-mitya-posudi',
             'https://sbermarket.ru/victoria/c/bitovaya-himiya-uborka-/osvezhiteli-aromatizatori',
             'https://sbermarket.ru/victoria/c/bitovaya-himiya-uborka-/chistyashchie-sredstva/dlya-kukhni?sort=popularity',
             'https://sbermarket.ru/victoria/c/bitovaya-himiya-uborka-/chistyashchie-sredstva/vanna-tualet',
             'https://sbermarket.ru/victoria/c/bitovaya-himiya-uborka-/chistyashchie-sredstva/sredstva-dlya-bitovoj-tekhniki',
             'https://sbermarket.ru/victoria/c/bitovaya-himiya-uborka-/chistyashchie-sredstva/dlya-prochistki-trub',
             'https://sbermarket.ru/victoria/c/bitovaya-himiya-uborka-/chistyashchie-sredstva/styokla-zerkala',
             'https://sbermarket.ru/victoria/c/bitovaya-himiya-uborka-/chistyashchie-sredstva/dlya-pola-kovrov-mebeli',
             'https://sbermarket.ru/victoria/c/bitovaya-himiya-uborka-/chistyashchie-sredstva/universalnie-sredstva']
    pages_name = ['Средства для стирки SBER ', 'Отбеливатели и пятновыводители SBER', 'Кондиционеры и ополаскиватели SBER', 'Средства для мытья посуды SBER', 'Освежители воздуха SBER', 'Средства для уборки кухни SBER', 'Средства для уборки ванной и туалета SBER', 'Средства для чистки бытовой техники SBER', 'Средства для чистки труб SBER', 'Средства для чистки стёкол SBER', 'Средства для чистки ковров и мебели SBER', 'Универсальные чистящие средства SBER']
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