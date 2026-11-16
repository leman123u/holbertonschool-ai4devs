#include <stdio.h>
#include <assert.h>

int sum_array(int arr[], int size)
{
	int total = 0;
	int i;

	for (i = 0; i < size; i++)
		total += arr[i];
	return (total);
}

int main(void)
{
	int numbers[] = {1, 2, 3, 4, 5};
	int single[] = {42};

	assert(sum_array(numbers, 5) == 15);
	assert(sum_array(single, 1) == 42);
	assert(sum_array(numbers, 0) == 0);
	printf("Sum: %d\n", sum_array(numbers, 5));
	printf("All bug4 tests passed\n");
	return (0);
}