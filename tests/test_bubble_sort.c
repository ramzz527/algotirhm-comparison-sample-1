#include <stdio.h>
#include <string.h>
#include "sort.h"

int main(void) {
    int input[] = {6, 8, 5, 9, 10, 1, 7, 2, 4, 3};
    const int want[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    bubbleSort(input, 10);
    if (memcmp(input, want, sizeof(want)) != 0) {
        fprintf(stderr, "bubble sort failed\n");
        return 1;
    }
    int duplicates[] = {3, 1, 3, 1, 2};
    const int sortedDuplicates[] = {1, 1, 2, 3, 3};
    bubbleSort(duplicates, 5);
    if (memcmp(duplicates, sortedDuplicates, sizeof(sortedDuplicates)) != 0) {
        fprintf(stderr, "bubble sort duplicate case failed\n");
        return 1;
    }
    return 0;
}