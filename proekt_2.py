from tkinter import *
import time
import random


class Platform:
    def __init__(self, canv: Canvas, colour):
        self.canvas = canv
        self.rect = canv.create_rectangle(230, 300, 330, 310, fill=colour)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

    def move(self):
        """Перемещает ракетку"""
        self.canvas.move(self.rect, self.x, 0)
        pos = self.canvas.coords(self.rect)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= 500:
            self.x = 0

    def left(self, event):
        self.x = -4

    def right(self, event):
        self.x = 4


class Ball:
    """Класс, который описывает мяч"""
    def __init__(self, canv: Canvas, colour, platform: Platform):
        self.canvas = canv
        self.oval = canv.create_oval(200, 200, 215, 215, fill=colour)
        self.plus = [2, 3, 4]
        self.minus = [-2, -4, -6]
        self.platform = platform
        self.x = random.choice([*self.minus, *self.plus])
        self.y = random.choice(self.minus)
        self.touch = False

    def move(self):
        """Перемещение объекта"""
        # Перемещает объект
        self.canvas.move(self.oval, self.x, self.y)
        # Возвращает значение координат мячика
        pos_oval = self.canvas.coords(self.oval)
        if self.check(pos_oval):
            self.y = random.choice(self.minus)
        if pos_oval[1] <= 0:
            self.y = random.choice(self.plus)
        elif pos_oval[3] >= 400:
            self.touch = True
        elif pos_oval[0] <= 0:
            self.x = random.choice(self.plus)
        elif pos_oval[2] >= 500:
            self.x = random.choice(self.minus)

    def check(self, ball_pos):
        platform_pos = self.canvas.coords(self.platform.rect)
        if platform_pos[1] <= ball_pos[3] < platform_pos[3]:
            if ball_pos[2] >= platform_pos[0] and ball_pos[0] <= platform_pos[2]:
                return True
        return False


window = Tk()
window.title('Пинг - Понг')
window.resizable(width=False, height=False)


canvas = Canvas(window, width=500, height=400)
canvas.pack()

platform = Platform(canvas, 'black')
ball = Ball(canvas, 'red', platform)


# Бесконечно прорисовывает окно и перемещает мяч
while not ball.touch:
    ball.move()
    platform.move()
    window.update()
    time.sleep(0.01)