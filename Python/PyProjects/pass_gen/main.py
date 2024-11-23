import random
import time
ran_sim_1 = "qwertyuiopasdfghjklzxcvbnm"
ran_sim_2 = "QWERTYUIOPASDFGHJKLZXCVBNM"
ran_sim_3 = "1234567890"
ran_sim_4 = "!@#$%^&*()_+{}|[]\\/.,<>"

all = ran_sim_1 + ran_sim_2 + ran_sim_3 + ran_sim_4

lenght = 8

password = "".join(random.sample(all, lenght))
print("Идет генерация пароля")
time.sleep(3)
print("Ваш пароль готов")

print(password)

input()

