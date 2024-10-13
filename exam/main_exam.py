from person import Person
from person import Action
from person import Work
from person import Rest

import random

person = Person(name='Микита', health=100, mood=100, money=0)
go_to_park = Rest(name = 'Сходить в парк', health=3, mood=15, money=0)
go_to_factory = Work(name = 'Пойти на завод', money = 50, mood = -10, health = -3)
go_to_hospital = Action(name = 'Пойти в больницу', money = -20, mood = -5, health = 20)




print(person)
person.change_state(money = random.randint(20, 100),
                    mood = random.randint(-20, -10),
                    health = random.randint(-10, -5))

print(person)
person.do(go_to_park)
print("Ви пройшлись по парку")
print(person)

person.do(go_to_factory)
print("Ви працювали на заводі та отримали гроші")

print(type(go_to_factory) == Work)

print(person)

person.do(go_to_hospital)
print("Ви пішли до поліклініки")
print(type(go_to_hospital) == Work)
print(person)