def problem_one():

	a = (34**2) 
	if a >= 17925:
		return ('a >= 17925')

	b = (26*3) 
	if b >= 17925:
		return ('b >= 17925')
	
	c = (17*33) 
	if c >= 17925:
		return ('c >= 17925')
	
	d = (4394*4)
	if d >= 17925 :
		return ('d >= 17925')
	else :
		return ('d <= 17925')

def test_problem_one():
	answer = 'd <= 17925'
	assert problem_one() == answer
	print('Testing is work!')


test_problem_one()


