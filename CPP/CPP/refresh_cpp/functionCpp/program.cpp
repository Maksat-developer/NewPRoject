#include <iostream>

using std::endl;
using std::cout;
using std::cin;


namespace firstSpace
{
  void foo()
{
  cout << "Message from function firstSpace: foo()" << endl;

}

struct point
{
  double x, y;
};


inline namespace params {
int global_a = 5;

}
}


namespace secondSpace
{
  void foo()
{
  cout << "Message from function secondSpace: foo()" << endl;

}

}


int main()
{
  int global_a = 10;


  firstSpace::point pt {};
  firstSpace::foo();
  secondSpace::foo();

  cout << global_a << " " << firstSpace::global_a << endl;


  return 0;

}