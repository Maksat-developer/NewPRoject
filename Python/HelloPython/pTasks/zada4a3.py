t = []
with open ('adik.txt', 'r') as ff:
    if 'w' in ff.read():
        print('есть буква "w" ')
    else:
        print('буквы "w" тут нет!')

