from requests import *
url = 'https://swapi.dev/api'
response = get(url).json()
planets_url = response['planets']
people_url = response['people']
info = {}


def get_planets():
    result = get(planets_url).json()
    for planet in result['results']:
        info[planet['name']] = planet['diameter']
    return info


planets = get(response['planets']).json()['results']


def compare(planets):
    diameter = 12742
    for i in planets:

        if int(i['diameter']) > diameter:
            print(f'Диаметр планеты {i["name"]} больше диаметра Земли на {int(i["diameter"]) - diameter} км.')

        elif int(i["diameter"]) < diameter:
            print(f'Диаметр планеты {i["name"]} меньше диаметра Земли на {diameter - int(i["diameter"])} км.')

        else:
            print(f'Диаметр планеты {i["name"]} равен диаметру Земли')
        print('.....')

