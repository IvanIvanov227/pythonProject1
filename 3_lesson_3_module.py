import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
from vk_api.utils import get_random_id

import wiki

TOKEN = 'vk1.a.Ud9SxvPcrUdauoIQ7g-903vAqDSJ8LjSUfRVbfXQT-_3cxxe4XuYSM_aw7Vs1kv3Y_hZ0F4-Ve4bE11bb3zgpZJb6xqkLxvwoJEX2BYC' \
        'Y7ah4oVpfT2ooadjIHdKtQESdUZCzCDax7UM-iYlsWU67U2nQ0qKwQivHiqKAfeagRcfLl4-3mRPAWsurx5q8G64TOSvIxT4HMxO2fiJzfaqyg'

# Подключаюсь к VK
vk = vk_api.VkApi(token=TOKEN)
vk._auth_token()
# Переопределили method
# vk = vk_session.get_api()

# Класс для работы с longpoll-сервером
longpoll = VkLongPoll(vk)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text.lower()
        user_id = event.user_id
        response = ''
        random_id = random.randint(1, 10 ** 10)
        # То же самое - random_id = get_random_id()
        if msg.lower() == 'привет':
            response = 'Привет'
        elif msg.startswith('-w'):
            ask = msg[3:]
            # Ограничение до 4000 символов, чтобы не было ошибки
            response = wiki.get_info_wiki(ask)[:4000]
        else:
            response = 'Не понял'
            # Отправляю сообщение
        vk.method('messages.send', {'user_id': user_id, 'random_id':random_id, 'message': response})