# Написать Функцию которая принимает предложение как аргумент,
# считает количество букв и возвращает сколько символов он ввёл. НЕ ИСПОЛЬЗОВАТЬ функцию len()

def predlojenie(a):
    my_list = []
    result = 0
    my_list.append(a)
    for my_list in a:
        result += 1
        print('spisok kolichestvo {0}'.format(result))

predlojenie('maksfmnksnklfs')
