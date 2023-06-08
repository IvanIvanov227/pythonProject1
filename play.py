import pygame as pg
import controls
from ball import Ball
from racket import Racket

def run():

    pg.init() #инициализвция самой игры
    screen = pg.display.set_mode((1250, 700)) #игровой экран, где все графич. элементы игры
    pg.display.set_caption("Пинг-понг") #название игрового окна
    bg_color = (0, 0, 0) #фоновый цвет экрана
    ball = Ball(screen) #получаем изображение
    racket = Racket(screen) #получаем ракетки

    while True:

        controls.events(racket) #обработка событий
        racket.update_racket() #обновляет позиции ракеток
        controls.update(bg_color, screen, ball, racket)

run()