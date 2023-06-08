import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today().strftime('%d.%m.%Y')

url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
date = {'date_req': today}

response = requests.get(url, params=date).content
xml = BeautifulSoup(response, 'lxml')


def course(valute_from, valute_to, amount):
    if valute_from == 'RUR':
        return round(amount / exchange_rates[valute_to], 2)
    else:
        return round(amount * exchange_rates[valute_from] / exchange_rates[valute_to], 2)


id_EUR = 'R01239'
id_USD = 'R01235'

exchange_rates = {
    'RUR': 1,
    'USD': round(float(xml.find('valute', {'id': id_USD}).value.text.replace(",", ".")), 2),
    'EUR': round(float(xml.find('valute', {'id': id_EUR}).value.text.replace(",", ".")), 2)
}

valute_from = 'EUR'
valute_to = 'USD'
amount = int(input(f'Сколько {valute_from} вы хотите конвертировать в {valute_to}: '))

result = course(valute_from, valute_to, amount)
print(f'{amount} {valute_from} равно {result} {valute_to}')