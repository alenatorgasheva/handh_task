import random

from errors.deadAttackError import DeadAttackError
from errors.wrongDefenseTypeError import WrongDefenseTypeError
from errors.wrongParamTypeError import WrongParamTypeError
from errors.wrongParamValueError import WrongParamValueError


class Creature:
    param_min = 1
    param_max = 20
    M = 1
    N = 6
    heal_max = 3

    def __init__(self, name, attack, armor, health, damage_min, damage_max):
        self.name = str(name)
        self.attack = self.check_param(attack)
        self.armor = self.check_param(armor)
        self.health_max = self.check_health(health)
        self.health = self.health_max
        self.alive = True
        self.heal_times = 0
        if damage_min < damage_max:
            self.damage = [damage for damage in range(damage_min, damage_max + 1)]
        else:
            self.damage = [damage for damage in range(damage_max, damage_min + 1)]

    def check_param(self, param):
        """Проверяем корректность Атаки и Защиты"""
        if isinstance(param, int):
            if self.param_min <= param <= self.param_max:
                return param
            raise WrongParamValueError("Один из параметров имеет неправильную величину.")
        raise WrongParamTypeError("Один из параметров имеет неправильный тип.")

    @staticmethod
    def check_health(param):
        """Проверяем корректность Здоровья"""
        if isinstance(param, int):
            if param > 0:
                return param
            raise WrongParamValueError("Один из параметров имеет неправильную величину.")
        raise WrongParamTypeError("Один из параметров имеет неправильный тип.")

    def action_heal(self):
        """Действие Исцеление"""
        if self.heal_times < 3:
            self.alive = True
            self.change_health(int(self.health_max * 0.5))
            self.heal_times += 1

    def action_attack(self, defense):
        """Действие Ударить"""
        if isinstance(defense, Creature):
            if self.alive:
                if self.check_success(defense):
                    damage = self.damage[random.randint(0, len(self.damage) - 1)]
                    defense.change_health(-damage)
                    return f"SUCCESS (урон = {damage})"
                return "FAILED"
            raise DeadAttackError("Мертвые существа не могут атаковать.")
        raise WrongDefenseTypeError("Атаковать можно только существ.")

    def check_success(self, defense):
        # Рассчитываем Модификатор атаки
        bonus = self.attack - defense.armor + 1

        # Проверяем успех удара
        for _ in range(bonus):
            dice = random.randint(1, 6)
            if dice >= 5:
                return True
        return False

    def set_name(self, name):
        self.name = str(name)

    def get_name(self):
        return self.name

    def set_attack(self, attack):
        self.attack = self.check_param(attack)

    def get_attack(self):
        return self.attack

    def set_armor(self, armor):
        self.attack = self.check_param(armor)

    def get_armor(self):
        return self.armor

    def set_health(self, health):
        self.health = self.check_health(health)

    def change_health(self, health_bonus):
        self.health += health_bonus
        if self.health <= 0:
            self.health = 0
            self.alive = False
        elif self.health > self.health_max:
            self.health = self.health_max

    def get_health(self):
        return self.health

    def get_alive(self):
        if self.alive:
            return "Alive"
        return "Dead"

    def get_heal_times(self):
        return self.heal_times

    def get_damage(self):
        return self.damage
