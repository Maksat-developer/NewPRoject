# Написать lambda которая получает сколько дней ПРОШЛО с нового года как
# параметр и говорит пользователю сколько дней ОСТАЛОСЬ до нового года.
from datetime import datetime
from datetime import datetime

def timeit(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper
@timeit
def rasshetgoda():
    byvwyigod = [2021]
    list = []
    print(list(map(lambda x: x + 1, byvwyigod)))
    print()






