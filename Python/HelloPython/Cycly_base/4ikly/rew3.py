countries_of_europe = ['Italy', 'France', 'Germany', 'Switzerland', 'Ireland']
for europe in countries_of_europe :
    client3 = input('куда вы летите из стран Евровпы? ')
    if client3==europe:
        print("Ваш рейс найден!")
        break
    else:
        print("Простите рейсов в эту страну пока нет...")
        break