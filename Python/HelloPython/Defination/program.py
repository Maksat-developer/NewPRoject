def minimal(l):
    min_number = l[0]
    for i in l:
        if i < min_number:
            min_number = i
    return  min_number



number_1 = [1, 3, 4, 6, 7, 2, 5]
min_1 = minimal(number_1)


number_2 = [2, 3.6, 4.1, 6, 7, 2, 5]
min_2 = minimal(number_2)

if min_1 < min_2:
    print(min_1)
else:
    print(min_2)
