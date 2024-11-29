from random import *
def random(number):
  	a = []
  	i = 0
  	while i < number:
  		s = randrange(0,1000)
  		if s in a :
  			continue
  		a.append(s)
  		i += 1
  	print(a)
random(number = int(input("Введите число: ")))
