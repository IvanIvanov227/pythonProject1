from random import *
import time


class Knight:
    def __init__(self):
        self.health = 100
        self.hit = 20


knight_1 = Knight()
knight_2 = Knight()
print('ИГРА НАЧАЛАСЬ\nЖЕЛАЕМ УДАЧИ!!!\n\n\n')
time.sleep(3)

while True:

    if knight_1.health > 0 and knight_2.health > 0:
        if randint(1, 2) == 1:
            knight_1.health -= knight_1.hit

            print('!!! Воин 2 ударил Воина 1 !!!')
        else:
            knight_2.health -= knight_2.hit
            print('!!! Воин 1 ударил Воина 2 !!!')

        print(f' - У Воина 1 осталось {knight_1.health} HP')
        print(f' - У Воина 2 осталось {knight_2.health} HP')
        print('.............................................')
        random_time = randint(1, 5)
        time.sleep(random_time)

    else:
        if knight_1.health == 0:
            print('Победу одержал ВОИН 2\nПоздравляем !!!')
        else:
            print('Победу одержал ВОИН 1\nПоздравляем!!!')
        break