#include <stdio.h>

int main()

{
	int a, b, c;
	printf("Введите два целых числа \n");

	scanf("%d%d", &a, &b);

	c = a + b;
	printf("Результат: %d + %d = %d \n", a, b, c);
	return 0;
}

