class House():
    def __init__(self, typehouse, areahouse):
        self.typehouse = typehouse
        self.areahouse = areahouse

    def get_house(self):
        self.totalarea = 0
        self.furnitures = {
            'Кравать' : 4,
            'Гардироб' : 2,
            'Стол' : 1.5
        }
        for value in self.furnitures.values():
            self.totalarea += value
        print('Тип дома: ',self.typehouse," -- Общая площадь:",self.areahouse, "\n",list(self.furnitures.keys()),"\n" "Оставшаяся площадь: " ,self.areahouse - self.totalarea)
b = House('Квартира', 80)
b.get_house()
