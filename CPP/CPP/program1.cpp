#include <iostream>

// using <пространство имен>::<элемент>;  
using std::cout;
using std::endl;
// using <alias> = <тип данных>;
using byte_8 = unsigned char;


namespace firstSpace {
    void foo()
    {
        cout << "Function from firstSpace: foo()"  << endl;
    }


inline namespace params {
    int global_a = 5;
}    
}


namespace secondSpace {
    void foo()
    {
        cout << "Function from secondSpace: foo()" << endl;
    }

struct point {};

int global_a = 10;

}

using point2D = secondSpace::point;





int main()
{
    firstSpace::foo();
    secondSpace::foo();

    cout << firstSpace::global_a << endl;

    cout << secondSpace::global_a << endl;

    point2D pt{};

    cout << "Hello World!" << endl;

    byte_8 ch;

}