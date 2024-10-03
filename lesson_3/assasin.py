from lesson_2.character import Character
import random


class Assasin(Character):


    def __init__(self, name, health, damage, defence):
        Character.__init__(self, name, health, damage, defence)

    def __str__(self):
        return Character.__str__(self)

    def attack(self, target):
        chance = random.random()
        probability_threshold = 0.5

        if chance < probability_threshold:
            damage = 1000
            return target.take_damage(damage)
        else:
            damage = self.damage
            return target.take_damage(damage)