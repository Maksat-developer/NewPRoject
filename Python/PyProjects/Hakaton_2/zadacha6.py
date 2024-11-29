import random as rd

print("Игра Угадай число. У Вас есть 3 попытки")
my_number = int(input("Введите число от 0 до 10: "))
print ("Ваше число: ", my_number)
random_number = rd.randint(0,10)
print("Загаданное число: ", random_number)
while my_number <= 10 and my_number >= 0:
    if my_number != random_number:
        print ("Вы не угадали, попробуйте ещё раз!", my_number)
        break
    if my_number == random_number:
        break
    else:
        break
print ("У Вас осталось ещё 2 попытки!")

my_number = int(input("Введите число от 0 до 10: "))
print ("Ваше число: ", my_number)
random_number = rd.randint(0,10)
print("Загаданное число: ", random_number)
while my_number <= 10 and my_number >= 0:
    if my_number != random_number:
        print ("Вы не угадали, попробуйте ещё раз!", my_number)
        break
    if my_number == random_number:
        break
    else:
        break
print ("У Вас осталась ещё 1 попытка!")
my_number = int(input("Введите число от 0 до 10: "))
print ("Ваше число: ", my_number)
random_number = rd.randint(0,10)
print("Загаданное число: ", random_number)
while my_number <= 10 and my_number >= 0:
    if my_number != random_number:
        print("Вы не угадали, попробуйте ещё раз!",my_number)
        break
    if my_number == random_number:
        break