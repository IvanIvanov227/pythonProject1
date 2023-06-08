from gtts import gTTS
import os
from random import choice
import pyglet

films = ['Чебурашка',
         'С лёгким паром!',
         'Чёрная пантера',
         'Титаник',
         'Один дома',
         'Железный человек',
         'Аватар',
         'Тачки',
         'Последнему игроку приготовиться',
         'Мстители',
         'Человек-Паук',
         'Король говорит',
         'По соображениям совести',
         'Такси',
         'Зелёная миля',
         'Король Лев']


def the_best_film():
    """Предлагает пользователю фильм"""
    film_user = input()
    i = 0
    while film_user == 'Фильм':
        answer = choice(films)

        tts = gTTS(text=answer, lang='ru')
        audio = f'audio{str(i + 1)}.mp3'
        tts.save(audio)
        with open(audio, 'rb') as f:
            # вместо mixer
            mus = pyglet.media.load('', f)
            mus.play()

        os.remove(audio)

        film_user = input()
        i += 1


the_best_film()