# # Задача 8:
### Множества:
months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
months_c = set(['decabr'])
# 1.Объединить 2 множества
# 2.Добавить месяц, которого нету во множестве
months_a.update(months_b,months_c)

# months_c = set(['decabr'])
# 3.Перебрать элементы множества
for i in months_a and months_b:
    print(i)
# 4.Вам даны 2 множества, узнать какие элементы пересекаются между ними.
# x = {1, 2, 3}
# y = {4, 3, 6}
