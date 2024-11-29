class Laptop:
    def __init__(self, model_name):
        self.model = model_name
        self.kharakteristics = []
        self.processor()
        self.ram()
        self.video_card()
        self.HDD()
        self.display_size()

    def processor(self):
       self.kharakteristics.append('Intel® Core™ i3-7020U CPU @ 2.30GHz × 4 ')

    def ram(self):
        self.kharakteristics.append('8 Гб DDR4')
    def video_card(self):
       self.kharakteristics.append('Mesa Intel HD Graphic')

    def HDD(self):
       self.kharakteristics.append('SSD 256 Гб')

    def display_size(self):
        self.kharakteristics.append('15,6 FHD')

laptop = Laptop(model_name='asus')
print(laptop.model)
print(laptop.kharakteristics)

class Lenovo:
    def __init__(self, Процессор, Оперативная_Память, Видеокарта, Жёсткий_Диск, Размер_экрана):
        self.Процессор = Процессор
        self.Оперативная_Память = Оперативная_Память
        self.Видеокарта = Видеокарта
        self.Жёсткий_Диск = Жёсткий_Диск
        self.Размер_экрана = Размер_экрана

    def get_Lenovo_info(self):
        print({'Процессор': self.Процессор, 'Оперативная Память': self.Оперативная_Память, 'Видеокарта': self.Видеокарта, 'Жёсткий Диск': self.Жёсткий_Диск, 'Размер_экрана': self.Размер_экрана})

s = Lenovo('Intel® Core™ i3-7020U CPU @ 2.30GHz × 4 ', '8 Гб DDR4' , 'Mesa Intel® UHD Graphics (CML GT2)', 'SSD  256,1 GB', '15.6')
s.get_Lenovo_info()
