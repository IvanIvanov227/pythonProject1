import requests
from bs4 import BeautifulSoup
from datetime import datetime
import contextlib


today = datetime.today().strftime('%d.%m.%Y')

url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
date = {'date_req': today}

# params позволяет передать второй аргумент в метод get()
response = requests.get(url, params=date).content
xml = BeautifulSoup(response, 'lxml')


@contextlib.contextmanager
def get_valute(id):
    try:
        valute = xml.find('valute', {'id': id})
        value_name = valute.find('name').text
        yield f'(1 шт.) {value_name} стоит(ят) {valute.value.text} руб.'
    except:
        yield 'Такой валюты нет'


value = input()
with get_valute(value) as currency:
    print(currency)