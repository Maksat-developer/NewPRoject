
# Задание 4:
        # Напишите программу, которая запрашивает у пользователя шесть вещественных чисел.
        # На экран выводит минимальное и максимальное из них, округленные до двух знаков после запятой.
        # Выполните задание без использования встроенных функций min() и max().

user = input('vvedi pervoe chislo')
user2 = input('vvedi vtoroe chislo')
list = []
list2 = []
for i in user:
    list.append(user)
    list2.append(user2)
    if list < list2:
        print('min', list)
    if list > list2:
        print('min', list2)
    else:
        pass