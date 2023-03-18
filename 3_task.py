"""
3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def user(name, surname, year_of_birth, city, mail, phone_number):
    user_data = {'name': name, 'surename': surname,
                 'year_of_birth': year_of_birth,
                 'city': city, 'mail': mail, 'phone_number': phone_number}
    print(
        f'Вы {surname} {name} {year_of_birth} года рождения, проживаете в городе '
        f'{city}. Ваш e-mail: {mail}, телефон: {phone_number}')


name = input('Введите свое имя: ')
surname = input('Введите свою фамилию: ')
year_of_birth = input('Введите Ваш год рождения: ')
city = input('Введите Ваш город проживания: ')
mail = input('Введите Ваш e-mail: ')
phone_number = input('Введите свой телефонный номер: ')
user(name=name, surname=surname, year_of_birth=year_of_birth, city=city,
     mail=mail, phone_number=phone_number)
