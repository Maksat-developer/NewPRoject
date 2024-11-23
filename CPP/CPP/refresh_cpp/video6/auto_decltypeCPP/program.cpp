#include <iostream>

using std::cout;
using std::cin;
using std::endl;


int main()
{
  int val = 0; // initialization
  int pow[] = {1, 2, 4, 8}; // massiv data

  double d(3.6);
  short sh(10); // functional notation

  char ch{'h'};  // braced initialization
  long lv{};

  int sum {1 + 3 + 4 + 5 + 6};
  double p (1 * 3.5 * 52.5 + 3);
  bool n_fl(false), t_fl(true);

  cout << d << " ()" << endl;
  cout << sh << " ()" << endl;

  cout << ch << " {}" << endl;
  cout << lv << " {}" << endl;

  cout << sum << " sum" << endl;
  cout << p << " p" << endl;
  cout << n_fl << " n_fl " << t_fl << " t_fl" << endl;


  // Константная переменная

  // c++11 auto

  return 0;
}