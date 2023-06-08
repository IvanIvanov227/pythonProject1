import requests
from bs4 import BeautifulSoup
from datetime import datetime


today = datetime.today().strftime('%d.%m.%Y')

url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
date = {'date_req': today}

# params позволяет передать второй аргумент в метод get()
response = requests.get(url, params=date).content
xml = BeautifulSoup(response, 'lxml')
valute = {}


def get_valute():
    for i in xml.find('valcurs'):
        valute[i.find('charcode').text] = i.get('id')
    return valute


def get_value(id):
    return xml.find('valute', {'id': id}).charcode.text, xml.find('valute', {'id': id}).value.text.replace(",", ".")

# USD
# code, val = get_value("R01235")
# print(f'На {today} 1 {code} стоит {round(float(val), 2)} рублей.')

# EUR
# code, val = get_value("R01239")
# print(f'На {today} 1 {code} стоит {round(float(val), 2)} рублей.')

# CNY - Китай
# code, val = get_value("R01375")
# print(f'На {today} 1 {code} стоит {round(float(val), 2)} рублей.')

# CAD - Канада
# code, val = get_value("R01350")
# print(f'На {today} 1 {code} стоит {round(float(val), 2)} рублей.')
