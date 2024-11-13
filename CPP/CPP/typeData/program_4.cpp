#include <iostream>

using std::cin;
using std::cout;
using std::endl;


int main()
{
    int val = 0;
    int pow[] = {1, 2, 4, 5};

    double d(-4.5);
    d = 5.78;


    short sh(10); // functional notation 
    char ch{'d'}; // braced initialization 
    long lv(5.43);


    int sum {2 + 3 + 4 + 5};
    double p (1 * 2.3 * 4.5 - 1);
    bool n_fl(false), t_fl(true);


    cout << sum << " " << p << endl;
    
    cout << sh << " " << d << endl;
    cout << ch << " " << lv << endl;

    return 0;

}