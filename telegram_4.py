from telebot import *
import requests
import random
from bs4 import BeautifulSoup
import parser


token = '5873886646:AAE36AuN7PDJQkfmbKlyHtFjODV4-gQC_3w'
bot = TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов и могу показать милых котиков!
    """
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button_1 = types.KeyboardButton('Факт')
    button_2 = types.KeyboardButton('Стихотворение')
    button_3 = types.KeyboardButton('Кошки')
    button_4 = types.KeyboardButton('Стикеры')
    button_5 = types.KeyboardButton('Во что поиграть?')
    keyboard.add(button_1, button_2, button_3, button_4, button_5)
    # Добавляет в клавиатуру кнопки
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)


@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    bot.send_message(message.chat.id, poem_text)
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    button = types.InlineKeyboardButton('Перейти', url='https://stihi.ru/')
    keyboard.add(button)
    bot.send_message(message.chat.id, 'Больше стихов читайте по ссылке', reply_markup=keyboard)


@bot.message_handler(commands=['fact'])
def send_fact(message):
    fact = parser.get_interesting_fact()
    bot.send_message(message.chat.id, f'Тема: {fact[0]}')
    bot.send_message(message.chat.id, f'Название факта: {fact[1]}')
    bot.send_message(message.chat.id, fact[-1])


@bot.message_handler(commands=['cat'])
def send_cat(message):
    url = parser.get_cat()
    bot.send_photo(message.chat.id, url)


@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    stic_id = 'CAACAgIAAxkBAAEHC4ZjrHprGubS5cjLmKPxtcRrlU5WQwACWAADZaIDLPRJoG9XuxmSLAQ'
    bot.send_sticker(message.chat.id, stic_id)


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.strip() == 'Факт':
        send_fact(message)
    elif message.text.strip() == 'Стихотворение':
        send_poem(message)
    elif message.text.strip() == 'Кошки':
        send_cat(message)
    elif message.text.strip() == 'Стикеры':
        send_sticker(message)
    elif message.text.strip() == 'Во что поиграть?':
        send_game(message)


@bot.message_handler(commands=['play'])
def send_game(message):

    markup = types.InlineKeyboardMarkup()
    button_a = types.InlineKeyboardButton('Экшен', callback_data='/action')
    button_b = types.InlineKeyboardButton('Приключения', callback_data='/adventure')
    button_c = types.InlineKeyboardButton('Инди', callback_data='/indie')
    button_d = types.InlineKeyboardButton('Ролевые игры', callback_data='?genres=rpg')
    button_e = types.InlineKeyboardButton('Шутеры', callback_data='/shooting')
    button_s = types.InlineKeyboardButton('Симуляторы', callback_data='/simulator')
    button_f = types.InlineKeyboardButton('Спорт и гонки', callback_data='?genres=sports,racing')
    button_t = types.InlineKeyboardButton('Стратегии', callback_data='/strategy')

    markup.row(button_a, button_b)
    markup.row(button_c, button_d)
    markup.row(button_e, button_s)
    markup.row(button_f, button_t)
    bot.send_message(message.chat.id, 'Какой жанр вы предпочитаете?', reply_markup=markup)


@bot.callback_query_handler(lambda call: True)
def handle(call):
    response = requests.get(f'https://www.gog.com/ru/games{call.data}')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    titles = html.find_all(class_='product-tile__title')
    games = []
    for title in titles:
        games.append(title.text.strip())
    bot.send_message(chat_id=call.message.chat.id, text=f'Рекомендую игру: {random.choice(games)}')
    bot.answer_callback_query(call.id)


bot.polling()