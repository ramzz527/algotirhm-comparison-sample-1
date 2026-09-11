#include "sort.h"

void insertionSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int value = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > value) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = value;
    }
}