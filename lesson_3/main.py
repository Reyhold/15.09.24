from lesson_2.character import Character
from assasin import Assasin



def attack_message(attacker: Character, target: Character, damage_done: float) :
    return f'{attacker.name} атакував {target.name}.\n' \
           f'{attacker.name} наніс {damage_done} шкоди. ' \
           f'У {target.name} залишилося {target.health} здоров`я.'


player1 = Character('Vasya', 150, 30, 20)
player2 = Assasin('Petya', 100, 20, 10)

print(f'Створено нового персонажа: {player1.name}')
print(f'Створено нового персонажа: {player2.name}')

player1.show_stats()
player2.show_stats()

while player1.health > 0 and player2.health > 0:
    damage_done = player1.attack(player2)
    print(attack_message(player1, player2, damage_done))

    damage_done = player2.attack(player1)
    print(attack_message(player2, player1, damage_done))

    print(f'{player1}\n{player2}')