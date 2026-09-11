#include <stdio.h>
#include <string.h>
#include "sort.h"

int main(void) {
    int input[] = {6, 8, 5, 9, 10, 1, 7, 2, 4, 3};
    const int want[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    shellSort(input, 10);
    if (memcmp(input, want, sizeof(want)) != 0) {
        fprintf(stderr, "shell sort failed\n");
        return 1;
    }
    int single[] = {42};
    shellSort(single, 1);
    if (single[0] != 42) {
        fprintf(stderr, "shell sort single case failed\n");
        return 1;
    }
    return 0;
}