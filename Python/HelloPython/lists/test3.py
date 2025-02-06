def memberAge(**age):
    for i, j in age.items():
        print(f'{i} is {j}')
        print(type(age))

memberAge(name='Alex', age=25, city='Moscow')









# def addNumber(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
#
# print(addNumber(1, 2, 3, 4, 5))
#
