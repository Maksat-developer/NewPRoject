import os
def mkdir():
    word1 = str(input('Назовите свою директорию: '))
    filee = open(word1, 'a+')
    filee.close()
mkdir()
