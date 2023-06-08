import random


class Tank:
    def __init__(self, model, armor, min_damage, max_damage, health):
        self.model = model
        self.armor = armor
        self.min_damage = min_damage
        self.max_damage = max_damage
        self.health = health
        self.status = True

    def shoot(self, enemy):
        damage = random.randint(self.min_damage, self.max_damage)
        enemy.health_down(damage)
        if not enemy.status:
            print(f'Командир, говорит экипаж {self.model}: танк {enemy.model} уничтожен')
            return True
        else:
            return False

    def health_down(self, damage):
        self.health -= damage / self.armor
        if self.health > 0:

            print(f'{self.model}: По нам попали, осталось {self.health}XP')
            return False
        else:
            self.health = 0
            self.status = False


class SuperTank(Tank):
    # Эти параметры можно использовать во всех методах класса
    def __init__(self, model, armor, min_damage, max_damage, health):
        # Это замена если бы писали self.model = model ... берём из класса Tank
        super().__init__(model, armor, min_damage, max_damage, health)
        self.forceArmor = True

    def health_down(self, damage):
        super().health_down(damage / 2)

