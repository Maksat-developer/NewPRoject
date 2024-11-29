def fibonachi():
    f1 = f2 = 1
    i = 0
    print("0 1",end = " ")
    while i < 7:
        f1, f2 = f2, f1 + f2
        i += 1
        print(f1, end = " ")
    print(f2)
fibonachi()
