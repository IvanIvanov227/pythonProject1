import vk_api
from api_centrobank import get_value, get_valute
from web_scraping import get_planets
from DZ_webscraping import max_speed
token = 'vk1.a.Ud9SxvPcrUdauoIQ7g-903vAqDSJ8LjSUfRVbfXQT-_3cxxe4XuYSM_aw7Vs1kv3Y_hZ0F4-Ve4bE11bb3zgpZJb6xqkLxvwoJEX2BYC' \
        'Y7ah4oVpfT2ooadjIHdKtQESdUZCzCDax7UM-iYlsWU67U2nQ0qKwQivHiqKAfeagRcfLl4-3mRPAWsurx5q8G64TOSvIxT4HMxO2fiJzfaqyg'
vk = vk_api.VkApi(token=token)
# аутентификация
vk._auth_token()
# вызывает другие методы
while True:
    messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})
    if messages['count'] >= 1:
        text = messages['items'][0]['last_message']['text']
        user_id = messages['items'][0]['last_message']['from_id']
        message_id = messages['items'][0]['last_message']['id']
        if text[:2] == '-к':
            course = get_value(get_valute()[text[3:]])
            vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': course})

        elif text.lower() == 'планеты':

            max_planet = max([int(value) for value in get_planets().values()])
            vk.method('messages.send', {'user_id': user_id, 'random_id': message_id,
                                        'message': f'Самый большой диаметр среди всех планет: {max_planet}'})

        elif text.lower() == 'корабли':
            speed = max_speed()
            vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': speed})

        else:
            vk.method('messages.send', {'user_id': user_id, 'random_id': message_id, 'message': text})