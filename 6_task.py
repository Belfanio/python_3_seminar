"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к
заданному числу X. Пользователь в первой строке вводит натуральное число
N – количество элементов в массиве. В последующих  строках записаны N целых
чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    6
    -> 5
"""
count_of_number = (input('Введите количество чисел: '))
desired_number = input('введите заданное число: ')
try:
    count_of_number = int(count_of_number)
    desired_number = int(desired_number)
except ValueError:
    print('Одно или несколько введенных значения не являються числом')
else:
    array = [int(input('Ввести число: ')) for i in range(count_of_number)]
    temporary_variable = [abs(array[i] - desired_number) for i in
                          range(len(array))]
    print(f'Наиболее близкое число к искомому '
          f'{array[temporary_variable.index(min(temporary_variable))]}')
