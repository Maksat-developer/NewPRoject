def sett(a,b,c,d):
    print(a)
    if a == set():
        return a
    else:
        a.pop()
        print(a)
        return sett(a)
    d = {'aaaa', '2df'}
sett(set(1))