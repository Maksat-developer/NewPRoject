from problem_3 import test_problem_three
def problem_seventeen():
    b = 5.6 
    h = 5.6
    j = 5.6
    batya = (b + h)
    ejje = (j * batya) 
    if ejje == 62.71999999999999:
        return ("62.71999999999999")

    else: 
        return ('Error')


test_problem_three(problem_seventeen(), '62.71999999999999')


