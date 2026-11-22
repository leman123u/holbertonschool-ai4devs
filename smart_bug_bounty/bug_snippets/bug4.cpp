
#include <iostream>
using namespace std;

int findMaximum(int numbers[], int size) {
    if (size <= 0) {
        return -1;
    }

    int maximum = numbers[0];

    for (int i = 1; i <= size; i++) {
        if (numbers[i] > maximum) {
            maximum = numbers[i];
        }
    }

    return maximum;
}

int main() {
    int numbers[] = {12, 45, 23, 67, 34};
    int size = 5;

    cout << "Maximum: " << findMaximum(numbers, size) << endl;

    return 0;
}
