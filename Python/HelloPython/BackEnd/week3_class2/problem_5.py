class Car:
     def __init__(self, make, model, year, odometer=0, fuel=70):
         self.make = make
         self.model = model
         self.year = year
         self.odometer = odometer
         self.fuel = fuel

     def drive(self, distance):
         fuel = distance / 10
         if self.fuel >= fuel:
             self.__add_distance(distance)
             self.__subtract_fuel(fuel)
             print('Let’s drive!')
         else:
             print('Need more fuel, please, fill more!')

     def __add_distance(self, distance):
        self.odometer += distance

     def __subtract_fuel(self, fuel):
        self.fuel -= fuel


a = Car('sedan', 'avto', '2020')


#a._Car__add_distance(100)


#a._Car__subtract_fuel(100)


print((a.drive(int('100'))
