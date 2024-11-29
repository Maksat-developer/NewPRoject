# def problem_two():

#     a = 10
#     b = 5
#     c = 11
    
#     d = a % 3 * 4.8
#     ba = b % 3 * 4.8
#     ca = c % 3 * 4.8
#     ha = d % 3 * 4.8
#     print (ba , ca , ha )

#     bakyt = 5
#     haha = 5
#     haba = bakyt == haha
#     print (haba)
#     jaj = 10
#     lege = 15
#     legend = jaj != lege 
#     print (legend)

# problem_two()

from problem_3 import test_problem_three
def problem_two():
    a = 10
    b = 5
    c = 11
    d = a % 3 * 4.8
    ba = b % 3 * 4.8
    ca = c % 3 * 4.8
    ha = d % 3 * 4.8

    if ba == 9.6:
        return ('9.6')

    if ca == 9.6:
        return ('9.6')

    if ha == 8.639999999999999:
        return ('8.639999999999999')

    else:
        return ('error')
        

test_problem_three(problem_two(),'9.6')
