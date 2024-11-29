class Cat:
    name = None
    age = None
    isHappy = None


    def __init__(self, name, age, isHappy):
        self.set_data( name, age, isHappy)
        self.get_data()


    def set_data(self, name, age, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy


    def get_data(self):
        print(self.name, f"age: {self.age}", f"isHappy: {self.isHappy}")


cat_1 = Cat("Barsik", 1, True)
cat_1.set_data("Jmorik", 5)


cat_2 = Cat("Jmot", 2, False)
