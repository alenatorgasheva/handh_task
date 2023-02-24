from creatures.monster import Monster
from creatures.player import Player
from errors.deadAttackError import DeadAttackError
from errors.wrongParamTypeError import WrongParamTypeError
from errors.wrongParamValueError import WrongParamValueError
import sys


def print_statistics(all_creatures):
    print("+", "-" * 39, "+", sep="")
    print("|\tname\t|\tЗдоровье\t|\tСтатус\t|")
    print("+", "-" * 39, "+", sep="")
    for creature in all_creatures:
        print(f"|\t{creature.get_name()}\t|\t\t{creature.get_health()}\t\t|\t{creature.get_alive()}\t|")
    print("+", "-" * 39, "+", sep="")


def main():
    all_creatures = []
    try:
        plant = Player("Plant", attack=10, armor=5, health=15, damage_min=1, damage_max=4)
        all_creatures.append(plant)
        zombie = Monster("Zombie", attack=7, armor=5, health=7, damage_min=1, damage_max=6)
        all_creatures.append(zombie)
        print_statistics(all_creatures)
    except WrongParamTypeError as e:
        print(e)
    except WrongParamValueError as e:
        print(e)
    else:
        try:
            print(f"\n> {plant.get_name()} attacks {zombie.get_name()} <")
            print("Результат:", plant.action_attack(zombie))
        except DeadAttackError as e:
            print(e)
        else:
            print_statistics(all_creatures)

        try:
            print(f"\n> {plant.get_name()} attacks {zombie.get_name()} <")
            print("Результат:", end=" ")
            print(plant.action_attack(zombie))
        except DeadAttackError as e:
            print(e)
        else:
            print_statistics(all_creatures)

        try:
            print(f"\n> {zombie.get_name()} attacks {plant.get_name()} <")
            print("Результат:", zombie.action_attack(plant))
        except DeadAttackError as e:
            print(e)
        else:
            print_statistics(all_creatures)

        try:
            print(f"\n> {plant.get_name()} attacks {zombie.get_name()} <")
            print("Результат:", plant.action_attack(zombie))
        except DeadAttackError as e:
            print(e)
        else:
            print_statistics(all_creatures)

        try:
            print(f"\n> {zombie.get_name()} attacks {plant.get_name()} <")
            print("Результат:", zombie.action_attack(plant))
        except DeadAttackError as e:
            print(e)
        else:
            print_statistics(all_creatures)


if __name__ == '__main__':
    print(sys.path)
    print("* ------------- START ------------- *\n")
    main()
    print("\n* -------------- END -------------- *")
