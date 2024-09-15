from character import Character

player1 = Character('Nik', 100, 3, 0)

print(f'Створено нового персонажа: {player1.name}')
print(f'У {player1.name} {player1.health} здоров`я')

incoming_damage = 20
print(f'{player1.name} отримав урон у кількості {incoming_damage}')
player1.health -= incoming_damage
print(f'У {player1.name} {player1.health} здоров`я')
player1.show_stats()