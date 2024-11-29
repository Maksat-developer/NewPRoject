
def lamba():
    a = [1745345, 98726, 439872634, 7312, 64872, 123687126, 9312, 4124, 231, 3123, 34, 3453]
    i = 0
    for i in a:
        sett = (lambda a,b: (b*a))(1.185, i)
        print(sett)
lamba()