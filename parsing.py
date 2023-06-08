import requests
from bs4 import BeautifulSoup
import random


def get_fact():
    response = requests.get('https://i-fakt.ru/') # Просим информацию с сайта
    response = response.content # Получаем HTML - код, c которым будем работать

    html = BeautifulSoup(response, 'lxml') # Чтобы с кодом работать ('lxml' - способ обработки нашего кода)
    fact = random.choice(html.find_all(class_='p-2 clearfix')) # выбирает случайно в списке один из фактов
    title = fact.find('h4').text # Из полученного элемента вытащим название факта
    url = fact.a.attrs['href'] # Обращаемся к атрибуту a и к конкретному аргументу (по ключу находим сайт)
    url2 = fact.find('a').attrs['href'] # Копия того, что написали выше
    return f'{title}, подробнее в источнике: {url}'


def get_event():
    response = requests.get('https://kudago.com/spb/festival/')
    response = response.content

    html = BeautifulSoup(response, 'lxml')
    fest = random.choice(html.find_all(class_='post-wrapper'))
    name = fest.find(class_='post-title-link').text.replace('\n', ' ')
    date = fest.find(class_='date-item').text.replace('\n', ' ')
    url = fest.a.attrs['href']
    print(f'Название меропритятия: {name}')
    print(f'Дата мероприятия: {date}')
    print(f'Подробнее на сайте:\n{url}')


def get_concert():
    response = requests.get('https://kudago.com/msk/concerts/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    concert = random.choice(html.find_all(class_='post-wrapper'))
    print(concert.find(class_="post-title-link").text.replace('\n', ''))
    print(concert.find(class_="date-item").text.replace('\n', ''))
    print(concert.a.attrs['href'])


answ = ''
while answ != 'Хватит':
    action = input('Факты, Мероприятия или Концерты?\n')
    if action == 'Факты':
        get_fact()
        print('-' * 100)
    elif action == 'Мероприятия':
        get_event()
        print('-' * 100)
    elif action == 'Концерты':
        get_concert()
        print('-' * 100)
    else:
        break