#include <iostream>

using std::cout;
using std::cin;
using std::endl;


int main()
{
    bool f1_print = false;
    // f1_print = true;
    wchar_t wch;
    wchar_t ch = 'd';

    wch = L'Я';

   
    wchar_t str_1[] = L"Привет мир!";
    ch = str_1[0];


    cout << sizeof(str_1) << endl;
    
   
    cout << ch << endl;

    // if(f1_print)
    // cout << "hi" << endl;

    // cout << str << endl;

    return 0;
}