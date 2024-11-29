# Создайте функцию которая генерирует 10 чисел Фибоначчи:

# 1,1,2,3,5,8,13,21,34,...
fib1 = fib2 = 1

n = int(input())

print(fib1, fib2, end=' ')

for i in range(10, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')