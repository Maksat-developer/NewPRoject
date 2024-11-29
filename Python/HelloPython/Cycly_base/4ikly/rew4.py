countries_of_central_asia = ['Kyrgyzstan', 'Kazakhstan', 'Tajikistan', 'Uzbekistan']
client2 = input('куда вы летите в central - Asia?')
for asia in countries_of_central_asia :
    if client2 == asia:
        print("Ваш рейс найден! Ваш класс (эконом)")
        break
    else:
        print("Простите рейсов в эту страну пока нет...")
        break