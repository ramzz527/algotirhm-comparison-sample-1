#include <stdio.h>
#include <string.h>
#include "sort.h"

int main(void) {
    int input[] = {6, 8, 5, 9, 10, 1, 7, 2, 4, 3};
    const int want[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    insertionSort(input, 10);
    if (memcmp(input, want, sizeof(want)) != 0) {
        fprintf(stderr, "insertion sort failed\n");
        return 1;
    }
    int reversed[] = {5, 4, 3, 2, 1};
    const int sortedReversed[] = {1, 2, 3, 4, 5};
    insertionSort(reversed, 5);
    if (memcmp(reversed, sortedReversed, sizeof(sortedReversed)) != 0) {
        fprintf(stderr, "insertion sort reversed case failed\n");
        return 1;
    }
    return 0;
}