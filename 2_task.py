"""
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).
Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!
Process finished with exit code 0
Пример:
Введите первое число: 10
Введите второе число: 10
1.0
Process finished with exit code 0
"""


def arithmetic_operation(first_number, second_number):
    arithmetic_result = first_number / second_number
    print(f'Результат деления первого числа на второе = {arithmetic_result}')


first_number = input('Введите первое число: ')
second_number = input('Введите второе число: ')
try:
    first_number = int(first_number)
    second_number = int(second_number)
    first_number/second_number
except ValueError:
    print('Одно или оба введенных значения не являються числом')
except ZeroDivisionError:
    print('Нельзя делить на 0')
else:
    arithmetic_operation(first_number, second_number)
