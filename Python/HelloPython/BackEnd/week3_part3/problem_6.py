def reg(x):
  login = input("Ведите логин : ")
  password = input("Ведите пороль: ")
  x(login,password)
@reg
def registratcia(login,password):
  k = 0
  for i in login:
    print(k+ord(i))
    break
  for i in password:
    print(k+ord(i))
    break
