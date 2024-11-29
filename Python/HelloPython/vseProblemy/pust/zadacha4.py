log = input('введи логин')
password = input('введи пароль')
snimok = input('вставь фото')
keylogger = {'log' : None, 'password' : None, 'snimok': None}
with open('loginst.txt', 'a') as ff:
     ff.write(log)
     ff.write(password)
     ff.write(snimok)
print(ff.read())
logg = keylogger['login'] = log
passwdd = keylogger['password'] = password
PHOTO = keylogger['snimok'] = snimok
ff.writelines('login : ' + log + ' ' + 'password : ' + password + 'photos : ' + PHOTO + '\n' )
# with open ('loginst.txt', 'r') as f:
#      print(f.read())
# f.close()

with open('loginst.txt', 'r') as ff:
     if log in ff.read() or password in ff.read() or snimok in ff.read():
          print(f'есть логин {log} ')
          print(f'есть пароль {password} ')
          print(f'есть фото {PHOTO} ')
     else:
          print('error')




log = input('введи логин')
password = input('введи пароль')
keylogger = {'log' : None, 'password' : None}
ff =  open('loginst.txt', 'w')
logg = keylogger['log'] = log
passwdd = keylogger['pass'] = password
ff.writelines('login : ' + logg +' ' + 'password : ' + passwdd + '\n' )
ff.close()
# with open ('loginst.txt', 'r') as f:
#           print(f.read())

with open ('loginst.txt', 'x') as ff:
     if log in ff.read() or password in ff.read() :
          print(f'есть логин {log} ')
          print(f'есть пароль {password} ')
     else:
          print('error')
