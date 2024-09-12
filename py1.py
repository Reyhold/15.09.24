while True:
    num1 = int(input('Введите число 1: '))
    num2 = int(input('Введите число 2: '))
    choice = input('Введите действие от 1-5(сумма, разница, произведение, деление и смена чисел соответственно) или 0 чтобы выйти: ')
    if choice == '1':
        result = num1 + num2
        print('Вышло:', result)
    elif choice == '2':
        result = num1 - num2
        print('Вышло:', result)
    elif choice == '3':
        result = num1 * num2
        print('Вышло:', result)
    elif choice == '4':
        if num2 != 0:
            result = num1 // num2
            print('Вышло:', result)
        else:
            print('На ноль делить нельзя')
    elif choice == '5':
        print('Возврат...')
    elif choice == '0':
        print('Отключение')
        break