# Напишите функцию которая принимает 2 Dictionary и добавляет вторую Dictionary к первой.
def dict(**kwargs):
    my_list = {'name':None,'lastname':None}

    if kwargs:
        my_list['name'] = kwargs['name']
        my_list['lastname'] = kwargs['firstname']
    print('list',my_list )

dict(
        name = 'maks',
        firstname = 'kydyrov'
)







