#include <iostream>

using std::cin;
using std::cout;
using std::endl;


int main()
{
  char msg[] = "I like C++ Language";


  for(char x : msg)
    cout << x << " ";

  return 0;
}
