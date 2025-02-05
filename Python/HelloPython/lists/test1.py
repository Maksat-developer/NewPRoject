
""" 
2. Напишите функцию, которая принимает список или
кортеж чисел. Функция должна возвращать результат по-
очередного сложения и вычитания чисел друг из друга.
Вызвав функцию plus_minus ([10, 20, 30, 40,
50, 60]), вы получите результат 10+20–30+40–50+60
или 50.

"""

# def plus_minus(numbers):
#     if not numbers:
#         return 0
    
#     result = numbers[0]

#     for index in range(1, len(numbers)):
#         if index % 2 == 1:
#             result += numbers[index]
#         else:
#             result -= numbers[index]

#     return result

# print(plus_minus([10, 20, 30, 40, 50, 60]))


"""
1. Напишите функцию, которая принимает список или кор-
теж чисел. Функция должна возвращать двухэлемент-
ный список, содержащий сумму чисел с четным индек-
сом и сумму чисел с нечетным индексом соответственно.
Вызвав функцию even_odd_sums ([10, 20, 30, 40,
50, 60]), вы получите [90, 120].
"""

# def even_odd_sums(numbers):
#     even_sum = 0
#     odd_sum = 0
#     for index, value in  enumerate(numbers):
#         if index % 2 == 0:
#             even_sum += value

#         else:
#             odd_sum += value

#     return(even_sum, odd_sum)
                

# result = even_odd_sums([10, 20, 30, 40, 50, 60])
# print(result)



