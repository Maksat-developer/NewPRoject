countries_of_east = ('Singapore', 'Malaysia', 'Indonesia', 'Hawaii')
client1 = ('Brazil', 'Canada', 'Kyrgyzstan', 'Italy', 'Argentina', 'Malasia')
for east in countries_of_east:
    if client1 == east:
        print("Ваш рейс найден! Ваш класс (Business)")
        break
    else:
        print("Простите рейсов в эту страну пока нет...")
        break

countries_of_central_asia = ['Kyrgyzstan', 'Kazakhstan', 'Tajikistan', 'Uzbekistan']
client2 = input('куда вы летите в central - Asia?')
for asia in countries_of_central_asia :
    if client2 == asia:
        print("Ваш рейс найден! Ваш класс (эконом)")
        break
    else:
        print("Простите рейсов в эту страну пока нет...")
        break

countries_of_europe = ['Italy', 'France', 'Germany', 'Switzerland', 'Ireland']
for europe in countries_of_europe :
    client3 = input('куда вы летите из стран Евровпы? ')
    if client3==europe:
        print("Ваш рейс найден!")
        break
    else:
        print("Простите рейсов в эту страну пока нет...")
        break
countries_of_america = ['Mexico', 'USA', 'Brazil', 'Columbia', 'Canada']
for america in countries_of_america:
    client4 = input('куда вы летите из стран USA? ')
    if client4==america:
       print("Ваш рейс найден!")
       break
    else:
        print("Простите рейсов в эту страну пока нет...")
        break



countries_of_east = ('Singapore', 'Malaysia', 'Indonesia', 'Hawaii')
client1 = ('Canada','Kyrgyzstan', 'Italy', 'Argentina', 'Malasia')
class0 = ('Business')
class1 = ('Middle')
class2 = ('Econom')
a = ('ваш рейс,,,')
b = ("Простите рейсов в эту страну пока нет...")
for i in client1:
   for ii in countries_of_east:
    if i == ii or i !=ii:
        print(a,i)
