class Zoo:
    def __init__(self, animal_1 = "Тигр",animal_2 = "Бегемот",animal_3 = "Лев"):
        self.animal_1 = animal_1
        self.animal_2 = animal_2
        self.animal_3 = animal_3
        self.animal_4 = [animal_2, animal_3]


p = Zoo()
print(p.animal_1, p.animal_2, p.animal_3,)
p.animal_1 = "Лев"
p.animal_3 = "Змея"
print(p.animal_1, p.animal_2, p.animal_3,"\n",p.animal_4)