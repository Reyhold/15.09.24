class Dead(Exception):
    def __init__(self, message):
        super().__init__(message)

class Depression(Exception):
    def __init__(self, message):
        super().__init__(message)

class Poor(Exception):
    def __init__(self, message):
        super().__init__(message)

class Action:
    def __init__(self, name='', health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class Work:
    def __init__(self, name='', health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class Rest:
    def __init__(self, name='', health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

class Person:
    def __init__(self, name='', health=0, mood=0, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f'== {self.name} ==\n' \
               f'Здоров`я: {self.health}\n' \
               f'Настрій: {self.mood}\n' \
               f'Фінанси: {self.money}\n'

    def do(self, action):
        self.money += action.money
        self.health += action.health
        self.mood += action.mood
        if self.mood > 90:
            self.money += 5
        if self.health < 40:
            self.mood -= 10

    def take_damage(self, health):
        self.health -= health
        if self.health <= 0:
            print("Ви не змогли вижити")
            raise Dead('Ви не змогли вижити')
        elif self.health == 0:
            print("Ваше здоров'я на нулі!")

    def change_mood(self, mood_change):
        self.mood += mood_change
        if self.mood <= 0:
            print("Ви божеволієте с кожним днем")
            raise Depression('Ви божеволієте с кожним днем')
        elif self.mood == 0:
            print("Ваш настрій на нулі!")

    def change_money(self, money_change):
        self.money += money_change
        if self.money <= 0:
            print("Ваш гаманець занадто пустий")
            raise Poor('Ваш гаманець занадто пустий')
        elif self.money == 0:
            print("Ваші фінанси на нулі!")

    def change_state(self, money, health, mood):
        self.money += money
        self.health += health
        self.mood += mood