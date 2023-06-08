import random


class User:
    """Обычный солдат"""
    def __init__(self, health, name):
        self.health = health
        self.name = name
        self.status = True

    def shoot(self, enemy):
        damage = random.randint(1, 10)

        enemy.reduce_health(damage)
        if not enemy.status:
            print(f'Боец {self.name} уничтожил {enemy.name}')

            return True
        else:
            print(f'{self.name} ранил {enemy.name}. Осталось {enemy.health}xp')
            return False

    def reduce_health(self, damage):
        self.health -= damage
        if self.health > 0:
            self.status = True
        else:
            self.health = 0
            self.status = False


class Magician(User):
    """Маг - восстанавливает здоровье"""
    def __init__(self, health, name, up_health):
        super().__init__(health, name)
        self.up_health = up_health

    def reduce_health(self, damage):
        res_lucky = random.randint(0, 1)
        if res_lucky:
            super().reduce_health(damage - self.up_health)
        else:
            super().reduce_health(damage)


class Warrior(User):
    """Воин - имеет броню"""
    def __init__(self, health, name, armor):
        super().__init__(health, name)
        self.armor = armor

    def reduce_health(self, damage):
        super().reduce_health(damage/self.armor)


class Archer(User):
    """Лучник - имеет больший удар"""
    def __init__(self, health, name, max_damage):
        super().__init__(health, name)
        self.max_damage = max_damage

    def shoot(self, enemy):
        damage = random.randint(10, self.max_damage)

        enemy.reduce_health(damage)
        if not enemy.status:
            print(f'Боец {self.name} уничтожил {enemy.name}')

            return True
        else:
            print(f'{self.name} ранил {enemy.name}. Осталось {enemy.health}xp')
            return False

    def reduce_health(self, damage):
        self.health -= damage
        if self.health > 0:
            return False
        else:
            self.health = 0
            self.status = False







