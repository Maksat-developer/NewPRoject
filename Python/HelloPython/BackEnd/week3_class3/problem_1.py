class Human:
    default_name= 'no name'
    default_age = '0'
    def __init__(self,name = default_name,age = default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = 0


    def info(self):
        print(f"Имя : {self.name} ")
        print(f'Возраст : {self.age}')
        print(f'Деньги : {self.__money}')
        print(f"Дом : {self.__house}")

    @staticmethod
    def default_info():
        print(f'Имя : {Human.default_name}\nВозраст : {Human.default_age}')


    def __make_deal(self,house,price):
        self.__house = house
        self.__money = price

    def earn_money(self,salary):
        self.__money += salary
        print(f'Вы заработали {salary} денег, ваш капитал {self.__money}')



    def buy_house(self,house,price):
        house_price = house.final_price(price)
        if self.__money >= house_price :
            self.__make_deal(house,house_price)
            print("у вас достаточна денег что бы купить дом ")
        else :
            print("Денег нет иди работай  бомж")

class House:
    def __init__(self , _area,_price):
        self._area = _area
        self._price = _price

    def final_price(self,discount):
        final_price = self._price * (100 - discount) / 100
        print(f"Цена со скидкой : {final_price}")
        return  final_price



class SmallHouse(House):
    default_area = 40
    def __init__(self,price):
        super().__init__(SmallHouse.default_area,price)


if __name__=="__main__":
    dastan = Human("Дастан",19)
    dastan.info()
    dastan.default_info()
    dastan.earn_money(10000)
    dastan.info()
    house = House(100,100000)
    smallHouse = SmallHouse(50000)
    dastan.buy_house(smallHouse,10)
    dastan.info()
    dastan.earn_money(20000)
    dastan.info()
    dastan.buy_house(smallHouse, 15)
    dastan.info()
    dastan.earn_money(40000)
    dastan.info()
    dastan.buy_house(house, 10)
    dastan.earn_money(40000)
    dastan.buy_house(house, 10)
    dastan.info()