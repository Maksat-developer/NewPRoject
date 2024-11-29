# Найти объекты которые есть и в 
# SET №2 и в 
# SET №3 
# из Google Colab

# Множество № 2:
farm_1 = {"dog", "cat", "mouse", "sheep"}

# Множество № 3:
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}


a = farm_1.intersection(farm_2)
b = farm_1.difference(farm_2)


print(a, b,)
