import pygame as pg

class Ball():

    def __init__(self, screen):
        """инициализация мячика"""

        self.screen = screen
        self.image = pg.image.load("мячик для ПП.png") #загружает изображение в наш проект
        self.rect = self.image.get_rect() #получили изображение как прямоугольник
        self.screen_rect = self.screen.get_rect() #получили экран как прямоугольник
        self.rect.center = self.screen_rect.center #мячик будет посередине экрана

    def output(self):
        """Отрисовывание мячика"""

        self.screen.blit(self.image, self.rect) #отрисовывает изображение, как прямоугольник
