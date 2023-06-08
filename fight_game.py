from participants import User, Magician, Warrior, Archer
import random


def game():
    user = User(150, 'Школьник')
    magician = Magician(80, 'Гарри Поттер', 5)
    warrior = Warrior(100, 'Вагнер', 2)
    archer = Archer(70, 'Соколиный глаз', 20)
    list_striker = [user, magician, warrior, archer]
    res_striker = random.choice(list_striker)
    list_striker.remove(res_striker)
    res_defender = random.choice(list_striker)
    while True:

        if res_striker.shoot(res_defender):
            print(f'Победил {res_striker.name}')
            break
        if res_defender.shoot(res_striker):
            print(f'Победил {res_defender.name}')
            break


game()


