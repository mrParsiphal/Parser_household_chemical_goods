import pandas as pd


def Converter(files, name_table):
    product = []
    mass_volume = []
    full_price = []
    discount_price = []
    name_shop = []
    for number_file in files:
        print(number_file)
        text = open(number_file, encoding='utf-8', mode='r')
        print('Read succesful')
        for stroke in text:
            stroke = str(stroke)
            stroke = stroke.replace('\xa0', '')
            print(stroke, end='')
            try:
                stroke_data.replace('в ассортименте', '')
            except: pass
            stroke_data = stroke.split()
            try:
                stroke_data.remove('Новинка!!!')
            except: pass
            try:
                stroke_data.remove('концентрат!!!')
            except: pass
            try:
                stroke_data.remove('₽')
                stroke_data.remove('₽')
            except: pass
            if stroke_data[-1] == '0' and stroke_data[-2] == '0':
                continue
            for i in range(len(stroke_data) - 2):
                if stroke_data[i].isdigit() and stroke_data[i + 1] in ('кг', 'мл', 'л', 'шт', 'ml', 'гр', 'г', 'литр', 'кг.', 'мл.', 'л.', 'шт.', 'ml.', 'гр.', 'г.', 'литр.', 'кг,', 'мл,', 'л,', 'шт,', 'ml,', 'гр,', 'г,', 'литр,'):
                    stroke_data[i] += stroke_data[i + 1]
                    stroke_data[i].replace(',', '')
                    stroke_data[i].replace('.', '')
                    stroke_data.pop(i + 1)
                    print(stroke_data)
                    break
            for i in range(len(stroke_data) - 2):
                if stroke_data[i][-1] == 'г' and stroke_data[i + 1] == 'х' and stroke_data[i + 2]:
                    stroke_data[i] += stroke_data[i + 1] + stroke_data[i + 2]
                    stroke_data.pop(i + 1)
                    stroke_data.pop(i + 2)
                    if stroke_data[i + 1] in ('гр'):
                        stroke_data[i] += stroke_data[i + 1]
                        stroke_data.pop(i + 1)
                    print(stroke_data)
                    break
            for i in range(len(stroke_data) - 2):
                if stroke_data[i][:2] == '1/':
                    stroke_data.pop(i)
                    print(stroke_data)
                    break
            print(stroke_data)
            discount_price.append(stroke_data[-1])
            full_price.append(stroke_data[-2])
            if stroke_data[-3][0].isdigit() and stroke_data[-3][-1].isalpha():
                mass_volume.append(stroke_data[-3])
                product.append(" ".join(stroke_data[:-3]))
            else:
                product.append(" ".join(stroke_data[:-2]))
                for i in range(len(stroke_data)):
                    if stroke_data[i][-2:] in ('л', 'г', 'g', 'l') or stroke_data[i][-2:] in ('кг', 'мл', 'шт', 'ml', 'гр'):
                        mass_volume.append(stroke_data[i])
                        break
                    if stroke_data[i][-4:] in ('кг.', 'мл.', 'л.', 'шт.', 'ml.', 'гр.', 'г.', 'литр.', 'кг,', 'мл,', 'л,', 'шт,', 'ml,', 'гр,', 'г,', 'литр,'):
                        patch = stroke_data[i]
                        patch.replace(',', '')
                        patch.replace('.', '')
                        mass_volume.append(patch)
                        break
                else:
                    mass_volume.append('None')
            print(stroke_data, end='\n\n')
            patch = number_file.split()
            number_shop = patch[-1][:-4]
            name_shop.append(number_shop)
    print('Data collected')
    data_for_exel = pd.DataFrame({'Товар': product, 'Вес/объём': mass_volume, 'Полная цена': full_price, 'Цена со скидкой': discount_price, 'Магазин': name_shop})
    data_for_exel.to_excel(f'./{name_table}.xlsx', sheet_name='parsed_data')



def Builder_exel():
    print('Run program')
    files = ['Средства для уборки METRO.txt',
             'Средства для уборки ZCOMETA.txt',
             'Средства для туалета ZCOMETA.txt',
             'Средства для мытья ванных комнат ZCOMETA.txt',
             'Средства для уборки SPAR.txt',
             'Средства для уборки OZON.txt',
             'Средства для чистки унитаза 5.txt',
             'Чистящие средства 5.txt',
             'Средства для чистки труб 5.txt']
    name_table = "Средства для уборки"
    Converter(files, name_table)
    files = ['Средства для стирки METRO.txt',
             'Средства для стирки ZCOMETA.txt',
             'Средства для стирки SPAR.txt',
             'Средства для стирки OZON.txt',
             'Средства для стирки 5.txt',
             'Пятновыводители 5.txt',
             'Жироудалители 5.txt']
    name_table = "Средства для стирки"
    Converter(files, name_table)
    files = ['Средства для мытья посуды METRO.txt',
             'Средства для мытья посуды ZCOMETA.txt',
             'Средства для мытья посуды SPAR.txt',
             'Средства для мытья посуды OZON.txt',
             'Средства для мытья посуды 5.txt']
    name_table = "Средства для мытья посуды"
    Converter(files, name_table)
    files = ['Освежители воздуха METRO.txt',
             'Освежители воздуха ZCOMETA.txt',
             'Освежители воздуха SPAR.txt',
             'Освежители воздуха OZON.txt']
    name_table = "Освежители воздуха"
    Converter(files, name_table)
    Converter(files, name_table)
    files = ['Средства для ухода за бытовой техникой OZON.txt',
             'Мыло OZON.txt']
    name_table = "Мыло и средства для ухода за бытовой техникой"
    Converter(files, name_table)


if __name__ == '__main__':
    Builder_exel()
