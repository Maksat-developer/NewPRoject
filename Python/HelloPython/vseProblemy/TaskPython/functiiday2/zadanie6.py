# Создайте функцию которая принимает слово и создаёт файл с таким
# именем в той же директории, где был запущен Ваш .py файл.
def nameFile():
    namefile = input('vvedi name file')
    ff = open(namefile, 'w')
    print(ff)
nameFile()