class Student:
  def __init__(self,name,lastname,age,objects):
    self.name = name
    self.lastname = lastname
    self.age = age
    self.objects = objects
  def disp(self):
    print(self.name, self.lastname, self.age, self.objects)

Steve = Student("Steven",'Shultz' , 23, "English")
Johny = Student("Jonathan","Rosenberg", 24 , "Biology")
Penny = Student("Penelope","Meramveliotakis", 21 , "Physics")
Steve.disp()
Johny.disp()
Penny.disp()
