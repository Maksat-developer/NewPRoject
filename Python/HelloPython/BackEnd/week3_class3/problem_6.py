from random import *
from time import *
class unit:
    def __init__(self,n,team):
        self.n = n
        self.team = team

class hero(unit):
    def __init__(self,name,n,team,level = 0):
        self.name= name
        self.level = level
        self.team=team
    def level_up(self, s):
        self.level+=s


Manas = hero("Манас",3914,"red")
Bakai = hero("Бакай",5536,"blue")

red_team = []
blue_team = []
class Oop(hero):
    voiny = int(input("Введите количество воинов: "))
    if voiny % 2 ==0:
        voiny +=1
    for i in range(1,voiny+1):
        d = choice([True,False])
        if d == True:
            red_team.append("Воин Манаса c номером "+str(i))

        else:
            blue_team.append("Воин Бакая c номером " +str(i))
    r,b=len(red_team),len(blue_team)

    if r > b:
        Manas.level_up(r//3)
        Bakai.level_up(b//5)
    elif r < b:
        Bakai.level_up(b//3)
        Manas.level_up(r//5)


    print("\nВ войске героя",Manas.name+"а"+",",str(Manas.level)+"-го уровня,",r,"воинов!")
    for x in red_team:
        print(x)
        sleep(0.2)

    print("\n"+"В войске героя",Bakai.name+"а"+",",str(Bakai.level)+"-го уровня,",b,"воинов!")
    for x in blue_team:
        print(x)
        sleep(0.2)

    print("\n ****НАЧАЛСЯ БОЙ МЕЖДУ ВОИНАМИ МАНАСА И БАКАЯ*** ")
    sleep(1)
    if r > b:
        g = 0
        for i  in blue_team:
            print(i,"умирает из рук",red_team[g],"и умерает сам" )
            sleep(0.2)
            b -=1
            r -=1
            g+=1
        print(f"\nВ Бою одержал победу Герой {Manas.name} {Manas.level}-го уровня, У него Осталось ",r,"воинов!")
    if r < b:
        g = 0
        for i  in red_team:
            print(i,"умирает из рук",blue_team[g],"и умерает сам" )
            sleep(0.2)

            r -=1
            g+=1
        print(f"\nВ Бою одержал победу Герой {Bakai.name} {Bakai.level}-го уровня, У него Осталось ",b,"воинов!")
    
