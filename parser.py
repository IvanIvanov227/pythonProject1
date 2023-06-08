import requests
import random
from bs4 import BeautifulSoup


def clear_spaces(string: str) -> str:
    string = string.strip()
    string = string.replace('\n', '')
    return string


def get_cat():
    page = random.randint(1, 49)
    url = f'https://yandex.ru/images/search?p={page}&text=котик&lr=2&rpt=image&uinfo=sw-1440-sh-900-ww-711-wh-680-pd-2-wp-16x10_2560x1600'
    response = requests.get(url)
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    url = random.choice(html.find_all(class_='serp-item__link')).attrs['href']
    return f'https://yandex.ru{url}'


def get_interesting_fact() -> tuple: # Означает, что возвращает кортеж
    response = requests.get('https://i-fakt.ru/fakty-po-rubrikam/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    rub = random.choice(html.find_all(class_='col-6 col-md-4'))
    rub_url = clear_spaces(rub.a.attrs['href'])
    rub_name = clear_spaces(rub.text.replace('\n', ''))
    response = requests.get(rub_url)
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    try:
        num = int(clear_spaces(html.find_all('li', class_='page-item')[-2].text))
        page = random.choice(range(1, num))
    except IndexError:
        page = 1
    rub_url += f'page/{page}/'
    response = requests.get(rub_url)
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    title = fact.find('h4').text
    url = fact.a.attrs['href']
    return rub_name, title, url


def get_event():
    response = requests.get('https://kudago.com/msk/festival/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    fest = random.choice(html.find_all(class_='post-content'))
    title = fest.find(class_="post-title-link").text.replace('\n', '')
    date = fest.find(class_="date-item").text.replace('\n', '')
    print(title)
    print(date)
    print(fest.a.attrs['href'])


def get_concert():
    response = requests.get('https://kudago.com/msk/concerts/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    concert = random.choice(html.find_all(class_='post-wrapper'))
    print(concert.find(class_="post-title-link").text.replace('\n', ''))
    print(concert.find(class_="date-item").text.replace('\n', ''))
    print(concert.a.attrs['href'])
