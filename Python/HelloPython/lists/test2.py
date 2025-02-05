"""
Напишите функцию sum_numeric, которая принимает
любое количество аргументов. Если аргумент является це-
лым числом или может быть преобразован в целое число,
то он должен быть добавлен к сумме. Аргументы, кото-
рые не могут быть преобразованы в целые числа, должны
быть проигнорированы. Результатом является сумма чисел.
Соответственно, sum_numeric (10, 20, ‘a’, ‘30’,
‘bcd’) вернет 60. Обратите внимание, что даже если
строка 30 является элементом списка, она преобразуется
в целое число и добавится к сумме.
"""

# def sum_numeric(*args):

#     total = 0
#     for arg in args:
#         try:
#             number = int(arg)
#             total += number
           
#         except ValueError:
#             pass
#     return total

# print(sum_numeric(10, 20, 'a', '30', 'bsd'))








"""
1. Напишите функцию mysum_bigger_than, которая ра-
ботает так же, как mysum, за исключением того, что она
принимает первый аргумент, предшествующий *args.
Этот аргумент задает максимальное значение аргумента,
которое можно добавить в сумму. Таким образом, вызов
mysum_bigger _than (10, 5, 20, 30, 6) вернет
50 — потому что 5 и 6 не больше, чем 10. Эта функция
аналогично работает с любым типом и предполагает, что
все аргументы имеют одинаковый тип. Обратите внима-
ние, что > и < работают с различными типами в Python,
а не только с числами. Для строк, списков и кортежей это
относится к их порядку сортировки.
"""

# def mysum_bigger_than(*args):
    
#     if not args:
#         return args
#     output = max(args[1:])
#     print(output)
    
#     for arg in args:
#         if arg > :
#             output += arg
#             return output

# print(mysum_bigger_than(10, 5, 20, 30, 6))



# def mysum_bigger_than(thershold, *args):
    
#     if not args:
#         return 0

#     total = 0
#     for arg in args:
#         if arg > thershold:
#             total += arg
        
#     return total

# print(mysum_bigger_than(10, 5, 20, 30, 6))


# def mySum(*args):
#     if not args:
#         return args
#     output = args[0]
#     print(f"output {output}")

#     for arg in args[1:]:
#         output += arg
#     return output

# print(mySum())
# print(mySum('a', 'b', 'c', 'd'))
# print(mySum([10, 20, 30], [40, 50, 60], [70,80]))
# print(mySum(10, 20, 30, 40))
