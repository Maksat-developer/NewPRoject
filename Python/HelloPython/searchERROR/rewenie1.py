# Представьте Вы хотите взять какой-то набор данных и переконвертировать его в SET
values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
print (values)
new_values = []
for i in values:
    try:
        set(i)
        new_values.append(True)
    except TypeError:
        new_values.append(False)
print (new_values)
print (all(new_values))
# для удаления дубликатов, в Classroom возьмите values и проверьте каждый ли элемент доступен


# для конвертации. Создайте список. Проитерируйте values. Если объект в списке можно переконвертировать
# добавьте True в новый список иначе добавьте False. После, с помощью функции
# all() скажите можно ли конвертировать values в SET?