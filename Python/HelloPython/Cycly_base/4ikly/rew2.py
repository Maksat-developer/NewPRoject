countries_of_east = ('Singapore', 'Malaysia', 'Indonesia', 'Hawaii')
client1 = ('Canada','Kyrgyzstan', 'Italy', 'Argentina', 'Malasia')
class0 = ('Business')
class1 = ('Middle')
class2 = ('Econom')
a = ('ваш рейс,,,')
b = ("Простите рейсов в эту страну пока нет...")
c = ('вам дан возможнность полететь класс middle')
for i in client1:
   for ii in countries_of_east:
    if i == ii or i !=ii:
        print(a,i)
