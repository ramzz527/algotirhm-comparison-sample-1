"""삽입 정렬."""


def insertion_sort(a):
    """a를 삽입 정렬로 제자리에서 오름차순 정렬한다."""
    for i in range(1, len(a)):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value
    return a