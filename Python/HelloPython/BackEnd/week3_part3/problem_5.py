import random
def ok(x):
    o = []
    for z in x():
        if z not in o:
            o.append(z)
    print(o)
    print(len(o))
@ok

def ko():
    a1 = []
    i = 0
    for i in range(100):
        b = random.randint(10, 50)
        a1.append(b)
        return a1
