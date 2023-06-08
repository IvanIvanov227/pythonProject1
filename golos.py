from pygame import mixer
# from gtts import gTTS
# import os
# import time
#
# # encoding, чтобы нормально прочитал текст (без иероглифов)
# with open('text.txt', 'r', encoding='utf-8') as file:
#     my_string = file.read()
# print(my_string)
#
# mixer.init()
#
# # Озвучивает текст на русском языке
# tts = gTTS(text=my_string, lang='ru')
#
# # Сохраняем файл
# tts.save('audio.mp3')
#
# # Загрузили текст
# mixer.music.load('audio.mp3')
#
# # Начало игры музыки
# mixer.music.play()
#
# while mixer.music.get_busy():
#     time.sleep(0.1)
#
# # Очищает за собой оперативную систему
# os.remove('audio.mp3')


import speech_recognition as sr

# Расшифровка текста
r = sr.Recognizer()

while True:
    # Подключение к микрофону
    with sr.Microphone(device_index=1) as source:
        print('Скажи что-нибудь')
        # Прослушка микрофона
        audio = r.listen(source)

    # Проверка ошибок, если сказали что-то непонятное
    try:
        # Расшифровка того, что мы сказали (нижний регистр на русском языке)
        speech = r.recognize_google(audio, language='ru_RU').lower()

    # Обрабатывается ошибка в случае, если речь непонятна
    except sr.UnknownValueError:
        print('Текст не распознан')
        
    else:
        print('Вы сказали:', speech)
