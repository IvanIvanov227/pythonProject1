from New_Tank import Tank, SuperTank
import random


def game():
    tank1 = Tank('Армата', 4, 100, 150, 600)
    tank2 = SuperTank('Leopard 2', 2, 80, 120, 600)
    while True:
        if tank2.shoot((tank1)):
            print(f'Победил {tank2.model}')
            break
        if tank1.shoot(tank2):
            print(f'Победил {tank1.model}')
            break


game()