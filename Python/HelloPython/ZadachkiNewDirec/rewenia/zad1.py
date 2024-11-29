list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
for i in list_1:
    for j in list_2:
        if i == j:
            c.append(i)
            break

print(c)