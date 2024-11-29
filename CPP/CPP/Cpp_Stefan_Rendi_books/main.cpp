#include <iostream>

using std::cout;
using std::cin;
using std::endl;
using std::string;


// Formule on matematic (x + 2) = y / 2 on C++ syntaxis 
int main()
{

    int nValue1, nValue2, nValue3;

    cout << "Введите три челых числа: " << endl;
    cin >> nValue1; 
    cin >> nValue2; 
    cin >> nValue3;

    
    // Вычисление среднего с использованием целочисленного деления
    int sum = nValue1 / 3 + nValue2 / 3  + nValue3 / 3 ; // Сумма чисел
    int average_int = sum / 3; // Целочисленное деление


    // Вычисление среднего с использованием чисел с плавающей точкой
    double average_double = static_cast <double>(sum) / 3; // Явное приведение к double


    cout << "Сумма чисел: " << sum << endl;
    cout << "Среднее целочисленное: " << average_int << endl;
    cout << "Среднее (с плаваюшей точкой): " << average_double << endl;
    

    return 0;
}
