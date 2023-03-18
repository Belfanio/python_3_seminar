"""
 Требуется вычислить, сколько раз встречается некоторое число X в массиве
 A[1..N]. Пользователь в первой строке вводит натуральное число
 N – количество элементов в массиве. В последующих  строках записаны
 N целых чисел Ai. Последняя строка содержит число X
*Пример:*
5
    1 2 3 4 5
    3
    -> 1
"""
import random

count_of_number = input('Введите количество элементов в массиве: ')
desired_number = input('Введите искомое число: ')
try:
    count_of_number = int(count_of_number)
    desired_number = int(desired_number)
except ValueError:
    print('Одно или несколько введенных значения не являються числом')
else:
    array = [random.randint(1, 5) for i in range(len(count_of_number))]
    print(array)
    print(f'Число {desired_number} встречается {array.count(desired_number)} раз')