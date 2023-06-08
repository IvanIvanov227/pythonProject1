import pygame as pg

class Racket():

    def __init__(self, screen):
        """Инициализация ракеток"""

        self.screen = screen
        self.image1 = pg.image.load("ракетка1.png")
        self.image2 = pg.image.load("ракетка2.png")
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.screen_rect = self.screen.get_rect()
        self.rect1.centery = self.screen_rect.centery
        self.rect2.centery= self.screen_rect.midright
        self.center1 = float(self.rect1.centery)
        self.center2 = float(self.rect2.centery)
        self.m_up1 = False
        self.m_down1 = False
        self.m_up2 = False
        self.m_down2 = False

    def draw_racket(self):
        """Создаёт ракетки и задаёт их положение"""
        self.screen.blit(self.image1, self.rect1)
        self.screen.blit(self.image2, self.rect2)

    def update_racket(self):
        """Обновление позиций ракеток"""
        if self.m_up1 and self.rect1.top >= self.screen_rect.top:
            self.center1 -= 1

        if self.m_down1 and self.rect1.bottom <= self.screen_rect.bottom:
            self.center1 += 1

        if self.m_up2 and self.rect2.top >= self.screen_rect.top:
            self.center2 -= 1

        if self.m_down2 and self.rect2.bottom <= self.screen_rect.bottom:
            self.center2 += 1

        self.rect1.centery = self.center1
        self.rect2.centery = self.center2










