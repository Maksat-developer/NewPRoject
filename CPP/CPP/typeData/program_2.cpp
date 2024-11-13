#include <iostream>

using std::cout;
using std::cin;
using std::endl;


int main()
{

    int* ptr_i = NULL;
    char* ptr_ch = nullptr; // c++ 11 
    void* ptr = 0L;


    ptr_i = (int *)ptr;
    ptr_ch = (char *)ptr_i;



    // ptr_i = (int *)malloc(sizeof(int) * 5 );

    printf("%p\n", ptr_ch);



    return 0;
}