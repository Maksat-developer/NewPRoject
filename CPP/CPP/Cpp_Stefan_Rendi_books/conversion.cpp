// Программа для преобразования
// градусов Цельсия в градусы Фаренгейта:
// Fahrenheit = NCelsius * (212 - 32)/100 + 32

#include <iostream>
#include <stdio.h>

using std::cout;
using std::endl;
using std::cin;


int main(int nNumberofArgs, char* pszArgs[])
{
    // Временные переменные - Заглушка 
    (void)nNumberofArgs;
    (void)pszArgs;
    
    // Введите температуру в градусах Цельсия
    int nNCelcius;
    cout << "Введите температуру по Цельсию: " << endl;
    cin >> nNCelcius;

    // для приведенной формулы преобразования
    //вычислим преобразующий множитель

    int nNFactor;
    nNFactor = 212 - 32;
    // используем вычисленный множитель для
    // преобразования градусов Цельсия в
    // градусы Фаренгейта
    int nFahrenheit;
    nFahrenheit =   nNFactor * nNCelcius / 100 + 32;

    // Ввыод результатов 

    cout << "Температура по фаренгейту: " << endl;
    cout << nFahrenheit << endl;


    return 0;
}
