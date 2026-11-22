
#include <iostream>
using namespace std;

int findMaximum(int numbers[], int size) {
    if (size <= 0) {
        return -1;
    }

    int maximum = numbers[0];

    for (int i = 1; i < size; i++) {
        if (numbers[i] > maximum) {
            maximum = numbers[i];
        }
    }

    return maximum;
}

int main() {
    int numbers1[] = {12, 45, 23, 67, 34};
    int numbers2[] = {-5, -2, -10};
    int numbers3[] = {100};

    cout << findMaximum(numbers1, 5) << endl;
    cout << findMaximum(numbers2, 3) << endl;
    cout << findMaximum(numbers3, 1) << endl;

    return 0;
}
