import os, random
# import os
# # Через Python у себя на рабочем столе создайте директорию,
os.mkdir('/Users/maksat.okulus/Documents/python/test.dir')
# # а внутри дериктории создайте 5 РАНДОМНЫХ файлов.
for i in range (5):
    with open ('/Users/maksat.okulus/Documents'
               '/python/test.dir' + str( random. randint(1, 100)) + '.txt', 'w') as file:
                file.write(str(i))
