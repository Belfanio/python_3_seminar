"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.
Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""
def print_message_from_list(month, month_list):
    if month == 1 or month == 2 or month == 12:
        print(f'Введенный месяц является {month_list[0]}')
    elif month == 3 or month == 4 or month == 5:
        print(f'Введенный месяц является {month_list[1]}')
    elif month == 6 or month == 7 or month == 8:
        print(f'Введенный месяц является {month_list[2]}')
    else:
        print(f'Введенный месяц является {month_list[3]}')
def print_message_from_dict(month, month_dict):
    print(f'Введенный месяц является {month_dict[month]}')

month_list = ['зимой', 'весной', 'летом', 'осенью']
month_dict = {'1':'зимой', '2':'зимой', '12':'зимой', '3':'весной', '4':'весной',
              '5':'весной', '6':'летом', '7':'летом','8':'летом', '9':'осенью',
              '10':'осенью','11':'осенью',}
month = input('Введите месяц числом: ')
try:
    month = int(month)
except ValueError:
    print('Введенное значение не является числом')
else:
    if int(month) < 1 or int(month) > 12:
        print('Введенное число не являеться месяцом')
    else:
        print_message_from_list(month, month_list)
        print_message_from_dict(str(month), month_dict)
