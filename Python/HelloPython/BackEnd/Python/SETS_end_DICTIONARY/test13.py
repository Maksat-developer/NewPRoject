# Из Google Colab Множество 4 и 5 



# Напишите код, который выведет новое множество, состоящее из животных,

# которые есть во второй ферме, но нет в первой.




# Множество № 2:
farm_1 = {"dog", "cat", "mouse", "sheep"}

# Множество № 3:
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}


list_1 = set()
a = farm_2.difference(farm_1)

list_1.update(a)

print(list_1)