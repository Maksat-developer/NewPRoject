# Создайте функцию которая принмает тип данных dictionary,
# но возвращает два Tuple в одном из них все ключи, в другом только значения.
def func(**kwargs):
    my_list = {'kluch1': None, 'kluch2': None}

    if kwargs:
        my_list['kluch1'] = kwargs['znacheniaKluxcha1']
        my_list['kluch2'] = kwargs['znacheniaKluxcha2']

    print('znachenia',my_list.values())
    print('keys', my_list.keys())

func(
    znacheniaKluxcha1 = 'door1',
    znacheniaKluxcha2 = 'door2'



)