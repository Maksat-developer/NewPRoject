# user = int(input("Введите число: "))
# #  получаем число от пользователя
#
# uslov = 0
#
# while user > 0:
#     digit = user % 10
#     print("Остаток в делении по модулю =", digit)
#
#     user = user // 10
#     print("Абсолютное деление =", user)
#
#     uslov  = uslov * 10
#     print("Умножаем на то что =", uslov)
#
#     uslov = uslov + digit
#     print(uslov)
#
#
# print('"Обратное" ему число =', uslov)



# a = 8
# while a > 7:
#     if a == 5:
#         print(a)
#         break
#     else:
#         print("Error")
#         break


# for i in range(1, 10):
#     if i == 5:
#         print(i, "Отчёт дошёл дл половины! ")
#         continue
#     print(i)


# items = ['молоко', 'сыр', 'творог', 'кефир', 'яблоко']
# for i, item in enumerate(items):
#     print(i + 1, item)

# count = 7
# while count < 117649:
#     print(count)
#     count *=7


# from pprint import pprint as pp
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# for i in a:
#     if i <= 5:
#         print(i, end="- ")
#     else:
#         print(f"Это числа больше 5 - ти = {i}")

#
# user = input("Введите число = ")
#
# srez = user[::-1]
# print('"Обратное" ему число =', srez)

# user = input("Введите число = ")
# # Берём чилос целое
#
# list_1 = list(user)
# # Переконвектируем его в Листы
#
# list_1.reverse()
# # Чтобы мы могли воспользоваться методом "reverse"
#
# other = "".join(list_1)
# # Слияние цифр
# print(f"Обратное цисло введенное вами {user} ==", other)

# d = 0
# while d < 5:
#     d += 1
#     print(d)

count = 10

while count > 0:
    if count == 15:
        break
    count += 1
    print(count)

