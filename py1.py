print('Привіт, як тебе звати?')
while True:
    a = input('Введіть ім`я: ')
    if not a:
        print('Будь-ласка повтори')
    else:
        print('Приємно познайомитись', a)
        break
# djsjdsdjsdj
while True:
    print('Скільки тобі років?')
    b = input('Введіть вік: ')
    if b >= '18':
        print('Нічого собі!')
    elif not b:
        print('Будь-ласка повтори')
    else:
        print('Ти ще такий молодий')
        break