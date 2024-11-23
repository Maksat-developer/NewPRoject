#include <iostream>
using std::cout;
using std::cin;
using std::endl;



int main()
{
  char str[100] = "Hi, Sergei";
  short old = 99;
  double weight = 59.3;


  cin >> str;
  // getline(cin, str);


  cout << str << "\n" << old << '\n' << weight << endl;

  return 0;

}
