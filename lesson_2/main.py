from character import Character

player1 = Character('Nik', 100, 3, 0)
player2 = Character('Alex', 100, 3, 0)

print(f'Створено нового персонажа: {player1.name}')
print(f'У {player1.name} {player1.health} здоров`я')
print(f'Створено нового персонажа: {player2.name}')
print(f'У {player2.name} {player2.health} здоров`я')

while True:
     print(f'{player1.name} атакував {player2.name}')
     player2.health -= player1.damage + 10
     print(f'У {player2.name} залишилося {player2.health}, після атаки {player1.name}'
           f'{player2.name} атакував у відповідь!')
     player1.health -= player2.damage + 10
     if player2.health <= 0:
         print(f'{player2.name} не переживе цю битву')
         break
     elif player1.health <= 0:
         print(f'{player1.name} не переживе цю битву')
         break