# numbers = [0, 1, 2, 3]
#
# EngList = ['<zero>', '<one>', '<two>', '<three>']
#
# for numbers, eng in zip(numbers, EngList):
#     print(f'{numbers} is {eng} in English')


upperCase = ['A', 'B', 'C', 'D', 'E', 'F']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f']

for i, (upper, lower) in enumerate(zip(upperCase, lowerCase), 1):
    print(f"{i} {upper} and {lower}")


