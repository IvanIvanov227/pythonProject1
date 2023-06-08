import telebot
import requests
import random
from bs4 import BeautifulSoup
import parser

token = '5873886646:AAE36AuN7PDJQkfmbKlyHtFjODV4-gQC_3w'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = """
    Привет! Я умею рассказывать стихи, знаю много интересных фактов, могу показать милых котиков и посоветовать, во что 
    поиграть!
    """
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=False)
    button_1 = telebot.types.KeyboardButton('Факт')
    button_2 = telebot.types.KeyboardButton('Стихотворение')
    button_3 = telebot.types.KeyboardButton('Кошки')
    button_4 = telebot.types.KeyboardButton('Стикеры')
    button_5 = telebot.types.KeyboardButton('Во что поиграть?')
    keyboard.add(button_1, button_2, button_3, button_4, button_5)
    # Добавляет в клавиатуру кнопки
    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)


@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и все стихотворенье..."
    bot.send_message(message.chat.id, poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button = telebot.types.InlineKeyboardButton('Перейти', url='https://stihi.ru/')
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


@bot.message_handler(commands=['Во что поиграть?'])
def send_game(message):
    response = requests.get('https://store.steampowered.com/search/')
    response = response.content
    html = BeautifulSoup(response, 'lxml')
    title = html.find_all(class_='title')
    games = [i.text for i in title]
    urls = []
    url_games = []
    for link in html.findAll('a'):
        urls.append(link.get('href'))
    for i in urls:
        if 'app' in i:
            url_games.append(i)
    url_and_game = {}
    for number in range(len(games)):
        url_and_game[games[number]] = url_games[number]
    random_game = random.choice(games)
    bot.send_message(message.chat.id, f'Игра: {random_game}')
    keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
    button = telebot.types.InlineKeyboardButton('Скачать', url=url_and_game[random_game])
    keyboard.add(button)
    bot.send_message(message.chat.id, 'Скачать можно по ссылке ниже', reply_markup=keyboard)


bot.polling()
