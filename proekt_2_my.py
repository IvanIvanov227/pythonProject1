import pygame
import sys
import random


def game():
    """Запуск игры"""
    # Инициализирует игру и создаёт объект экрана
    pygame.init()

    width = 900
    height = 650
    bg_color = (22, 242, 125)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Пинг - Понг')

    # Создаём надпись на экране, которая указывает, как начать игру
    # создаём шрифт
    font = pygame.font.SysFont('Times New Roman', 30)
    # создаём текст
    black = (0, 0, 0)
    text = font.render('Чтобы начать, нажми Enter', True, black)
    # определяем координаты текста на экране
    text_rect = text.get_rect()
    text_rect.center = (470, 150)

    # Создание ракеток
    racket_1 = Racket(screen, 'red', 1, 'Игрок_1')
    racket_2 = Racket(screen, 'blue', 2, 'Игрок_2')

    # Создание и перемещение мячика
    ball = Ball('white', screen, racket_1, racket_2)

    # Флаг, при нажатии Enter начинается игра
    game_start = False

    # Основной цикл игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN and not game_start:
                    game_start = True
                    text = font.render('', True, (255, 255, 255))

                if game_start:
                    if event.key == pygame.K_w:
                        racket_1.status = True
                        racket_1.direct = 'up'
                    elif event.key == pygame.K_s:
                        racket_1.status = True
                        racket_1.direct = 'down'
                    elif event.key == pygame.K_UP:
                        racket_2.status = True
                        racket_2.direct = 'up'
                    elif event.key == pygame.K_DOWN:
                        racket_2.status = True
                        racket_2.direct = 'down'

        # Цикл перерисовывает экран при каждом своём проходе
        screen.fill(bg_color)

        # Рисунок границы
        pygame.draw.line(screen, 'white', [width // 2, 50], [width // 2, height], 2)
        pygame.draw.line(screen, black, [0, 50], [width, 50], 2)

        # Отображение количества очков у игроков
        text_name_1 = font.render(f'{racket_1.name}: {ball.win_count_1}', True, black)
        text_name_2 = font.render(f'{racket_2.name}: {ball.win_count_2}', True, black)

        # Отображение мячика
        ball.move()
        if game_start:
            ball.update()

        # Отображение ракеток
        if racket_1.status:
            racket_1.update(racket_1.direct)
        racket_1.move()
        if racket_2.status:
            racket_2.update(racket_2.direct)
        racket_2.move()

        # Рисуем текст на экране
        screen.blit(text, text_rect)
        screen.blit(text_name_1, (50, 13))
        screen.blit(text_name_2, (550, 13))

        # Отображение последнего прорисованного экрана
        pygame.display.flip()


class Racket:
    """Ракетка для Пинг - Понга"""

    def __init__(self, screen, colour, number, name):
        self.colour = colour
        self.screen = screen
        self.y = 0.2
        self.racket_y = 300
        if number == 1:
            self.rect = pygame.Rect(20, self.racket_y, 10, 100)
        elif number == 2:
            self.rect = pygame.Rect(870, self.racket_y, 10, 100)
        self.direct = ''
        self.name = name
        self.status = True

    def move(self):
        """Отображение ракетки на экране"""
        self.rect.y = self.racket_y
        pygame.draw.rect(self.screen, self.colour, self.rect)
        if self.racket_y <= 52 or self.racket_y >= 550:
            self.status = False

    def update(self, direction):
        """Беспрерывно перемещает ракетку"""
        if self.status:
            if direction == 'down':
                self.racket_y += self.y
            elif direction == 'up':
                self.racket_y -= self.y


class Ball:
    """Мячик"""

    def __init__(self, colour, screen, racket1, racket2):
        self.screen = screen
        self.colour = colour
        self.racket1 = racket1
        self.racket2 = racket2
        self.x = random.choice([-0.2, 0.2])
        self.y = random.choice([-0.2, 0.2])
        self.x_ball = 450
        self.y_ball = 350
        self.rad = 10
        self.win_count_1 = 0
        self.win_count_2 = 0
        self.square_circle = pygame.Rect((self.x_ball - self.rad, self.y_ball - self.rad,
                                                        self.rad, self.rad))

    def move(self):
        """Отображение мячика на экране"""
        pygame.draw.circle(self.screen, self.colour, (self.x_ball, self.y_ball), self.rad)

    def update(self):
        """Обновляет позицию мячика"""
        self.x_ball += self.x
        self.y_ball += self.y
        if self.collide_circle_square():
            self.x *= -1
            # Ускорение мячика
            if self.x > 0:
                self.x += 0.003
            else:
                self.x -= 0.003
        if (self.x_ball - self.rad) >= 900:
            self.win_count_1 += 1
            self.start()
        if (self.x_ball + self.rad) <= 0:
            self.win_count_2 += 1
            self.start()
        if self.y_ball <= 52:
            self.y *= -1
        if self.y_ball >= 650:
            self.y *= -1

    def collide_circle_square(self):
        """Обрабатывает столкновения круга и квадрата"""
        self.square_circle.x = self.x_ball
        self.square_circle.y = self.y_ball
        collide1 = pygame.Rect.colliderect(self.square_circle, self.racket1)
        collide2 = pygame.Rect.colliderect(self.square_circle, self.racket2)
        if collide1 or collide2:
            return True

    def start(self):
        """После забитого гола ставит мяч и ракетки на стартовые позиции"""
        self.racket1.racket_y = 300
        self.racket2.racket_y = 300
        self.x = random.choice([-0.2, 0.2])
        self.y = random.choice([-0.2, 0.2])
        self.x_ball = 450
        self.y_ball = 350
        pygame.time.delay(1000)


if __name__ == '__main__':
    game()