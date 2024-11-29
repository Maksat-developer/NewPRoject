def menu():
    a = open('menu.txt', 'w')
    menuFood = input('Что вы хотите заказать поесть?\n')
    menuDrink = input('Что вы хотите заказать выпить?\n')
    a.write(menuFood)
    a.write(menuDrink)
    a.write('')
    a.close()
menu()