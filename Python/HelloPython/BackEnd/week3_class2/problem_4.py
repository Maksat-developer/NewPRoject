class Airplane:
    def __init__(self, make = ' Boing', model = '757', year = '2016', max_speed = '600 km/h', odometer = '10,000 m', is_flying = False):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = odometer
        self.is_flying = is_flying
    def take_off(self):
        is_flying = True
        land = False
        print('Взлет')
    def fly(self):
        is_flying = True
        land = False
        print('Летит',self.max_speed, self.odometer)
    def land(self):
        is_flying = False
        land = True
        print('Приземление')

a = Airplane()
a.take_off()
b = Airplane()
b.fly()
c = Airplane()
c.land()