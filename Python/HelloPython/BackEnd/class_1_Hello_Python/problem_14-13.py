from problem_3 import test_problem_three
def problem_14_13():
    a = 6
    b = 13
    c = 17.6
    d = 7
    e = 26
    batya = (a-e**(b/d))%c
    if batya == 3.9684630526765545:
        return ('3.9684630526765545')
    else:
        return ('Error')

test_problem_three(problem_14_13(), '3.9684630526765545')

