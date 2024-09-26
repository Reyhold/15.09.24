import datetime

class Student:
    def __init__(self, name='', age=2008, mark=10, group='B29158'):
        self.name = name
        self.age = age
        self.mark = mark
        self.group = group

    def __str__(self):
        return f'== {self.name} ==\n' \
               f'Год рождения: {self.age}\n' \
               f'Средний балл: {self.mark}\n' \
               f'Группа: {self.group}\n'

    def get_age(self):
        datetime.date.today()