// Это перва программа на C++


#include <iostream>


namespace firstSpace {
void foo()
{
	std::cout << "fuction from firstspace: foo()"  << std::endl;
}
}

struct point {
	double x, y;
};





namespace secondSpace {
void foo()
{
	std::cout << "fuction from secondspace: foo()" << std::endl;		
}
}





int global_a = 5;


int main()
{
	int global_a = 15;
	point {};
	firstSpace::foo();
	secondSpace::foo();
	std::cout << global_a <<  " " << ::global_a << std::endl;
	
	return 0;

}
  
