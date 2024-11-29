def problem_three():

    a = (16 + 18)
    b = a * 43
    c = b ** b
    bakyt = b - 193432
    if bakyt != -191970:
        return ('Error')
    else :
        return ('-191970')

def test_problem_three(answer,problem):
    assert problem == answer
    print('Testing is work!')




