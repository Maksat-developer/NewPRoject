с = input('введи слово!')
l = len(с)
l = l//2
for i in range(l):
    if с[i] != с[-1-i]:
        print('это не палиндром ')
        quit()
print('это полиндром')
