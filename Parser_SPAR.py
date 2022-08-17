import requests
from bs4 import BeautifulSoup
import time

def Parser():
    pages = ['https://spar-online.ru/catalog/bytovaya_khimiya_tovary_dlya_uborki/sredstva_dlya_stirki/?SHOWALL_1=1',
             'https://spar-online.ru/catalog/bytovaya_khimiya_tovary_dlya_uborki/sredstva_dlya_uborki/?SHOWALL_1=1',
             'https://spar-online.ru/catalog/bytovaya_khimiya_tovary_dlya_uborki/sredstva_dlya_mytya_posudy/?SHOWALL_1=1',
             'https://spar-online.ru/catalog/bytovaya_khimiya_tovary_dlya_uborki/osvezhiteli/?SHOWALL_1=1']
    pages_name = ['Средства для стирки SPAR', 'Средства для уборки SPAR', 'Средства для мытья посуды SPAR', 'Освежители воздуха SPAR']
    for j in range(len(pages)):
        url = f'{pages[j]}'
        headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }
        response = requests.get(url, headers=headers)
        page = response.text
        soup = BeautifulSoup(page, 'lxml')
        block = soup.find_all("div", {"class": "item_info"})
        list = []
        for i in range(len(block)):
            title = block[i].find("a")
            text = title.text
            span_price_with_discount = block[i].find("span", {"class": "price_value rty"})
            if span_price_with_discount != None:
                text += ' ' + span_price_with_discount.text.strip()
                span_price = block[i].find("span", {"class": "price_value vbn"})
                text += ' ' + span_price.text
            else:
                span_price = block[i].find("span", {"class": "price_value fgh"})
                text += ' ' + span_price.text + ' 0'
            print(text)
            list.append(text)


        with open(f'{pages_name[j]}.txt', encoding='utf-8', mode='w') as result:
            for i in list:
                result.write(i + '\n')
        time.sleep(1)

if __name__ == '__main__':
    Parser()
