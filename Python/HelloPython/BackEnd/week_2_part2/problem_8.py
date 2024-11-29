def prostye_chisla():
	print('Алгоритм нахождения простых чисел')
	a = eval(input('Введите конечное число: '))
	for num in range(a):
		prime = True
		for i in range(2,num):
			if (num%i==0):
				prime = False
		if prime:
			print (num)
prostye_chisla()