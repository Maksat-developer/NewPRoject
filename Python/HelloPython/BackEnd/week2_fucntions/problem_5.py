import random
def get_number():
	a = ('1', '4', '5', '7', '9', '0')
	k = []
	i = 0
	while i < 6:
		q = random.choice(a)
		k.append(q)
		i+=1
	print(k)
get_number()