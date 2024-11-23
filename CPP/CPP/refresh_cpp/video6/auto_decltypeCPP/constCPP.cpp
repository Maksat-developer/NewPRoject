#include <iostream>

using std::cout;
using std::endl;
using std::cin;


int main()
{

  const double pi {3.1415};

  auto first_num = 10;
  auto second_num = 5;
  auto name = 'Maks';
  auto d_ouble = 5.3;
  auto type_float = 0.3f;

  auto unsing_int = 5u;
  auto unsing_log = (short)10 + 10000UL;

  int *ptr = nullptr; // Указатель
  int k;
  int& lk = k; // Ссылка

  auto t1 = k;
  auto t2 = *ptr;
  auto t3 = ptr;
  auto t4 = &ptr;
  auto t5 = lk;
  


  cout << pi << endl;

  return 0;

}