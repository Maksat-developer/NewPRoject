class Student:
    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance
    def get_student_info(self):
        print(self.name, self.lastname,', поступил в', self.year_of_entrance, 'году, в учебное заведение:', self.department)
per = Student('Шайырбеков', 'Бакыт', 'Специалист информационной безопасноти', '2022')
per.get_student_info()