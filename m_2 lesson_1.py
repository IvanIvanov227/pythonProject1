def calculator(p_1, p_2, operation):
    """Функция - калькулятор"""

    try:

        p_1 = int(p_1)
        p_2 = int(p_2)
        if operation == '+':
            print(f'Результат: {p_1 + p_2}')
        elif operation == '-':
            print(f'Результат: {p_1 - p_2}')
        elif operation == '*':
            print(f'Результат: {p_1 * p_2}')
        elif operation == '/':
            print(f'Результат: {p_1 / p_2}')
        else:
            print('Ошибка синтаксиса')
            print('Давай заново!')
            print('-' * 100)
            a = input('Введи первое число: ')
            b = input('Введи второе число: ')
            op = input('Введи операцию(+, -, *, /): ')
            calculator(a, b, op)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
        print('Давай заново!')
        print('-' * 100)
        a = input('Введи первое число: ')
        b = input('Введи второе число: ')
        op = input('Введи операцию(+, -, *, /): ')
        calculator(a, b, op)
    except ValueError:
        print('Проверь, число ли ты ввёл')
        print('Давай заново!')
        print('-' * 100)
        a = input('Введи первое число: ')
        b = input('Введи второе число: ')
        op = input('Введи операцию(+, -, *, /): ')
        calculator(a, b, op)


print('Привет! \nВведи любые два числа и операцию\nИ я выведу тебе ответ!')
print('-' * 100)
p_1 = input('Введи первое число: ')
p_2 = input('Введи второе число: ')
opper = input('Введи операцию(+, -, *, /): ')
calculator(p_1, p_2, opper)