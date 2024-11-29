# Напишите код где есть TypeError,IndexError,NameError.
try:
        B = asda
        print('gmeromgoe')
except NameError :
        print('error')


try:
        B = (1,2,3,4,6)
        print(B[6])
except IndexError :
        print('error')

try:
        B = str(1, 2, 3, 4, 6)
        print(B[6])
except TypeError:
        print('error')

