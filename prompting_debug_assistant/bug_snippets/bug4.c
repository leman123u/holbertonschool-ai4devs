#include <stdio.h>

int sum_array(int arr[], int size)
{
	int total = 0;
	int i;

	for (i = 0; i <= size; i++)
		total += arr[i];
	return (total);
}

int main(void)
{
	int numbers[] = {1, 2, 3, 4, 5};

	printf("Sum: %d\n", sum_array(numbers, 5));
	return (0);
}