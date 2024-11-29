def rec(n):
    if n < 20 and n %2 !=2:
        print(n)
        rec(n+2)
        print(n)
rec(1)