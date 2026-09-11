"""버블 정렬."""


def bubble_sort(a):
    """a를 제자리에서 오름차순으로 정렬한다."""
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            return a
    return a