from problem_3 import test_problem_three
def problem_four():
	a = (17*3)
	b = (12*5)
	if a < b :
		return ("a < b")
	c = (12**3) 
	d = (13*7)
	if c < d :
		return ("c < d")
	i = (4**5) 
	l = (512+512)
	if i > l :
		return ("i > l")
	else :
		return(a , b , c , d , i , l)

test_problem_three(problem_four(), "a < b")




