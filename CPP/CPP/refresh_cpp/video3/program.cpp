#include <iostream>
// using <пространство имен>::<элемент>

using std::endl;
using std::cout;
using std::cin;


// using <alias> = <typeData>
using byte_8 = unsigned char;


namespace firstSpace {
  void foo()
  {
    cout << "Message from firstSpace func: foo()" << endl;
  }


struct point {
  double x, y;
};

}


using point2D = firstSpace::point;


namespace secondSpace {
  void foo()
  {
    cout << "Message from secondSpace func: foo()" << endl;
  }

int global_a = 5;

}


int main()
{
  byte_8* ptr_ch, *a;


  firstSpace::foo();
  secondSpace::foo();

  point2D pt {};

  cout << secondSpace::global_a << endl;

}
