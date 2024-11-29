x = []
for i in range(1,11):
    x.append(i)
t = str(x[0:-1] + x[::-1])
w = list(t)
w.remove(']')
w.remove('[')
print(t[::-1])