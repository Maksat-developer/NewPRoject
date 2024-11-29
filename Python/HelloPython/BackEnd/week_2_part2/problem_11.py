def problema(name, cash = 5000):
    a = input('Введите свою зарплату: ')
    if a == '':
        print(name, '-', cash )
    else:
        print(name, '-', a)
problema(name = input('whats your name ? : '))
