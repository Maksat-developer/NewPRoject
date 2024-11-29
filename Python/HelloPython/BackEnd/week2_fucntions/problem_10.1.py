import random
name = input('ваше имя : ')
act1 = input("камень ножницы бумага")
act = ["Камень" ,"Ножницы","Бумага"]
comp = random.choice(act)
print(comp)
if act1 == 'камень' and comp == "Ножницы":
    print(name,"winner")
if act1 =='ножницы' and comp =='Бумага':
    print(name,'winner')
if act1 == 'бумага' and comp == "Камень":
    print(name,"winner")
if act1 =='камень' and comp =='Бумага':
    print('PC is winner')
if act1 == 'бумага' and comp == "Ножницы":
    print(name,"winner")
if act1 =='ножницы' and comp =='Камень':
    print('PC is winner')
if act1 == 'камень' and comp == "Камень":
    print(name,"winner")
if act1 =='ножницы' and comp =='Ножницы':
    print(name,'winner')
if act1 == 'камень' and comp == "Ножницы":
    print(name,"winner")
if act1 =='бумага' and comp =='Бумага':
    print(name,'winner')