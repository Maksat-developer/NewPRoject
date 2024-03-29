#include <stdio.h>

int main()

{
	int a, b, result;
	printf("Введите два целых числа \n");

	scanf("%d%d", &a, &b);

	result = a + b;
	printf("Result: %d + %d = %d", a, b, result);
	return 0;
}

