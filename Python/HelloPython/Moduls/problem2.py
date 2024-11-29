import random
# Вам дан список
import random

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat",
         "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
list = []
i = 0
while True:
    rand_name = random.choice(names)
    if rand_name not in list:
        list.append(rand_name)
        i+=1
    if i == 4:
        break
print(list)

#  и вытащите 4 рандомных имени оттуда и сохраните в другой список.



