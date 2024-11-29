import random

spis_simvolov = '1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./'

vvod_pass = int(input('Количество паролей'))
dlina = int(input('Длина строки'))

for i in range(vvod_pass):
    password = ''
    for ii in range(dlina):
        password += random.choice(spis_simvolov)

    print(password)
