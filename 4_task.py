"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def my_func(first_number, second_number, third_number):
    all_number = [first_number, second_number, third_number]
    all_number.sort()
    sum_of_numbers = all_number[1] + all_number[2]
    print(f'Сумма двух наибольших аргументов = {sum_of_numbers}')
    if all_number[0]< all_number[1] < all_number[2]:
        sum_of_number = all_number[1] + all_number[2]
    elif all_number[1] < all_number[0] < all_number[2]:
        sum_of_number = all_number[0] + all_number[2]
    else:
        sum_of_number = all_number[0] + all_number[1]
    print(f'Сумма двух наибольших аргументов = {sum_of_numbers}')


first_number = input('Введите первое число: ')
second_number = input('Введите второе число: ')
third_number = input('Введите третье число: ')
try:
    first_number = int(first_number)
    second_number = int(second_number)
    third_number = int(third_number)
except ValueError:
    print('Одно или несколько введенных значения не являються числом')
else:
    my_func(int(first_number), int(second_number), int(third_number))
