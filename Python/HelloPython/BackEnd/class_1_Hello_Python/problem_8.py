from problem_3 import test_problem_three
def problem_eight():
    a = 2021
    b = 100
    c = (a/b)*100
    print(c)
    if c == 2021.0:
        return ('2021.0')
    else:
        return ('Error')

test_problem_three(problem_eight(), '2021.0')

