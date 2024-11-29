import datetime
import time


class Soldier:
    name = "no name"
    gun = "ak47"
    def __init__(self, name, gun):
        self.name = name
        self.gun = gun

class Guns():
    def shoots(self):
        print(f'{Soldier.name} shoots from: {Soldier.gun}')
        self.ammunition = 30
        while self.ammunition > 0:
            self.ammunition -= 1
            print('tigi-tigitishh')
            time.sleep(0.5)

        if self.ammunition == 0:
            self.reloads()
        else:
            pass


    def reloads(self):
        self.reload = input('Do you want to reload weapon? y/n: ')
        if self.reload == 'y':
            self.shoots()
        else:
            pass


class Act_of_Shooting(Soldier, Guns):
    def init(self, name, gun):
        Soldier.init(self, name, gun)

bakyt = Soldier("Bakyt",'Ak47')
soldier1 = Act_of_Shooting('Soldier Ryan', 'AK47')
soldier1.shoots()

