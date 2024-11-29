# Создайте функцию которая которая берёт лист делит его пополам и
# обе стороны разворачивает в противоположную сторону. Пример:
#
# Оригинальный Лист:
import random
def perebor():

    list_1 = ['name', 'age', '1', '19']
    list_2 = []
    for i in list_1:
            delim = random.choice(list_1)
            list_2.append(delim)
            print(list_2)

perebor()
