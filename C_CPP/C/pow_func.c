#include <stdio.h>
#include <math.h>



int main() {
	double base, exponent, result;

	base = 2.0;
	exponent = 3.0;
	result = pow(base, exponent);
	printf("%.1f В степени %.1f равно %.2f\n", base, exponent, result);
	return 0;
}
