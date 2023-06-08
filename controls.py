import pygame as pg
import sys

def events(racket):
    """Обработка события"""
    for event in pg.event.get():  # получаем все события пользователя
        if event.type == pg.QUIT:  # если тип события равен крестику
            sys.exit()  # выход

        elif event.type == pg.KEYDOWN: #если нажали на кнопку
            if event.key == pg.K_w:
                racket.m_up1 = True

            if event.key == pg.K_s:
                racket.m_down1 = True

            if event.key == pg.K_UP:
                racket.m_up2 = True

            if event.key == pg.K_DOWN:
                racket.m_down2 = True

        elif event.type == pg.KEYUP: #если отжали кнопку
            if event.key == pg.K_w:
                racket.m_up1 = False

            if event.key == pg.K_s:
                racket.m_down1 = False

            if event.key == pg.K_UP:
                racket.m_up2 = False

            if event.key == pg.K_DOWN:
                racket.m_down2 = False

def update(bg_color, screen, ball, racket):
    """Обновление экрана"""
    screen.fill(bg_color)  # заливка фона
    ball.output()  # рисует изображение на экран
    racket.draw_racket()  # рисует ракетки
    pg.display.flip()  # прорисовка последнего экрана








