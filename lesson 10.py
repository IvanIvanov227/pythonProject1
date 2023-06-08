import requests
from bs4 import BeautifulSoup
import random

response = requests.get('https://store.steampowered.com/?l=russian')
response = response.content

html = BeautifulSoup(response, 'lxml')

fact = html.find_all(class_='gutter_item')
list_1 = []
list_2 = []
list_3 = []

for p_1 in fact:
    list_1.append(p_1.text)
for p_2 in list_1:
    for p_3 in p_2:
        if '\r' in p_3:
            list_2.append(p_2)
for p_4 in list_2:
    list_3.append(p_4.strip())

games = {'Бесплатно': ['War Thunder', 'Brawlhalla', 'Dota 2'],
         'Ранний доступ': ['Valheim', 'SCUM', 'Brotato'],
         'Гонки': ['Wreckfest', 'Crossout', 'ShowRunner'],
         'Инди': ['Terraria', 'Aim Lab', 'Stray'],
         'Казуальная игра': ['Stardew Valley', 'Among Us', 'Bloons TD 6'],
         'ММО': ['Path of Exile', 'Albion Online', 'DayZ'],
         'Приключение': ['Rust', 'Raft', 'The Forest', 'NARAKA: BLADEPOINT'],
         'Ролевая игра': ['Hades', 'Black Desert', 'Slay the Spire'],
         'Симулятор': ['Cutues: Skylines', 'Aim Lab', 'RimWorld'],
         'Спортивная игра': ['Fishing Planet', 'TRAIL OUT', 'TEKKEN 7'],
         'Стратегия': ['PUBG: BATTLEGROUNDS', 'Hearts of Iron IV', 'Crusader Kings III'],
         'Экшен': ['UNDECEMBER', 'left 4 Dead 2', 'ELDEN RING']
}
def user_games():
    print('ИГРОВЫЕ ЖАНРЫ:\n')

    for p_5 in list_3:
        print(f'- {p_5}')

    print('-' * 100)
    genre_user = input('Какой из данных жанров вы больше всего предпочитаете?\n')

    for game in games:
        if game == genre_user:
            print(f'Для вас подойдёт игра: {random.choice(games[game])}')

user_games()
