from requests import *
# from random import *

url = 'https://swapi.dev/api'
response = get(url).json()
starships_api = get(response['starships']).json()

max_speed_all = {}
# five_max_speed = {}

for info in starships_api['results']:
    speed_starships = info['max_atmosphering_speed']
    if speed_starships == 'n/a':
        continue
    if 'km' in speed_starships:
        speed_starships = speed_starships[0:-2]

    max_speed_all[info['name']] = int(speed_starships)

# random_names_starships = []
# for name in max_speed_all.keys():
#     random_names_starships.append(name)
# while len(five_max_speed) < 5:
#     random_name = choice(random_names_starships)
#     if random_name not in five_max_speed:
#         five_max_speed[random_name] = max_speed_all[random_name]

max_speed_starships = 0
name_first_starships = ''


def max_speed():
    global  max_speed_starships, name_first_starships
    for ship_name, ship_speed in max_speed_all.items():
        if ship_speed > max_speed_starships:
            max_speed_starships = ship_speed
            name_first_starships = ship_name
    return f'Самый быстрый корабль "{name_first_starships}" имеет скорость {max_speed_starships}'




