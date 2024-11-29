from problem_3 import test_problem_three
def telegram_two():

	a = 4
	b = 7
	if a % 2 == 0:
		return ("Число четное")
	if a % 2 == 1  or a % 2 < 4:
		return ("Число простое")
	else:
		return ("Число 4 оположительное или простое")
	# print(f"Число {a} оположительное или простое ")

test_problem_three(telegram_two(), "Число 4 оположительное или простое")

# Error