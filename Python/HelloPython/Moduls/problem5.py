import random
# Возьмите список имён из задания №2 и
Group = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar",
         "Bolotbek", "Alymbek", "Dastan", "Maksat"]
#
# сформируйте 4 разные команды из всех участников.
red_com = []
blue_com = []
black_com = []
silver_com = []
comandred = 'Красная команда'
comandblack = 'Черная команда'
comandsilver = 'Команда серебра'
comandblue = 'Команда синих'


i = 0
while True:
    rand_name = random.choice(Group)
    if rand_name not in red_com:
        red_com.append(rand_name)
        i+=1
    if i == 4:
        break
print(comandred,red_com)

i = 0
while True:
    rand_name = random.choice(Group)
    if rand_name not in blue_com:
        blue_com.append(rand_name)
        i+=1
    if i == 4:
        break
print(comandblue,blue_com)


i = 0
while True:
    rand_name = random.choice(Group)
    if rand_name not in black_com:
        black_com.append(rand_name)
        i+=1
    if i == 4:
        break
print(comandblack,black_com)


i = 0
while True:
    rand_name = random.choice(Group)
    if rand_name not in silver_com:
        silver_com.append(rand_name)
        i+=1
    if i == 4:
        break
print(comandsilver,silver_com)