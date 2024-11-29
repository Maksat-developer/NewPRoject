from problem_3 import test_problem_three
def telegram_one():

	f = 10
	r = 10.5
	j = 13.7 
	if r > j :
		return ("r > j")
	elif r < j:
		return ("r < j")
	elif r == j:
		return ("r = j")
	if telegram_one() == r < j:
		return ('r < j')
	else :
		return ('Error')
test_problem_three(telegram_one(), 'r < j')


	
