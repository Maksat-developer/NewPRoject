import sys
a = input('введи первое значение :')
b = input('введите второе значение :')
print (sys.getsizeof(a))
print (sys.getsizeof(b))
if a > b :
    print('первое занимает больше памяти')
else:
    print('второе занимает больше памяти')