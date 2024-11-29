# создайте форму решистрации которая спрашивает у пользователся лог пар и фото
log = input('введи логин: ')
password = input('введи пароль: ')
photo = input('полный путь до фото: ')
raswirenia = ['png', 'img', 'mp3']

f = open('sudo.txt', 'a')
f.write (log + password + photo)
with open('sudo.txt', 'r') as ff:
    for i in ff.read():
        for ii in raswirenia:
            if photo == raswirenia:
              print('Регистрация прошла успешна')
ff.close()