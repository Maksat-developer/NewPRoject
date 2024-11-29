from random import randrange

game = '''И так Компьютер играем
в камень ножницы бумага.
    1.Камень
    2.Ножницы
    3.Бумага

'''
superUser = int(input('введите число: '))
print(superUser)
if superUser == 1:
    print('Вы выбрали камень/n')

elif superUser == 2:
    print('Вы выбрали Ножницы/n')

elif superUser == 3:
        print('Вы выбрали Бумага/n')

else:
    print('error')

comp = randrange(3) + 1
print(comp)
if comp == 1:
    print('Выбор компа камень/n')

elif comp == 2:
    print('Выбор компа Ножницы/n')

elif comp == 3:
        print('Выбор компа Бумага/n')


superUser = int(input('введите число: '))
print(superUser,comp)
if superUser == comp
    print('Это ничья/n')

elif comp == 1 and superUser == 2 or comp == 2 and superUser ==3 or comp == 3 and == 1:
    print('Вы выбрали Ножницы/n')

elif superUser == 3:
        print('Вы выбрали Бумага/n')
