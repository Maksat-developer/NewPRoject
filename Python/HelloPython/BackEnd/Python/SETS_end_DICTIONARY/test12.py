# Из Google Colab Множество 4 и 5

# Напишите код, который: Выведет новое множество, которое есть как в

# первой ферме, так и во второй.

# Множество № 2:
farm_1 = {"dog", "cat", "mouse", "sheep"}

# Множество № 3:
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}


list_1 = set()
a = farm_1.intersection(farm_2)

list_1.update(a)

print(list_1)
