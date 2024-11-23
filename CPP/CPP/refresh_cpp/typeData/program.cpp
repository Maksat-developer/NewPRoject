#include <iostream>

using std::cin;
using std::endl;
using std::cout;


int main()
{
  bool fl_print = false;

  wchar_t wch;
  wchar_t ch1 = 'd';
  // char ch2 = 'Я';
  wchar_t str[] = L"Привет мир!";
  ch1 = str[0];

  wch = L'Я';

  cout << "Длина str[] = " << " " << sizeof(str) << endl;


  cout << "wch = " << " " << wch << endl;
  cout << "ch1 = " << " " << ch1 << endl;
  // cout << "ch2 = " << " " << ch2 << endl;

  return 0;

}