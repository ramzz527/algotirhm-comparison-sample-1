"""셸 정렬."""


def shell_sort(a):
    """a를 셸 정렬로 제자리에서 오름차순 정렬한다."""
    gap = len(a) // 2
    while gap > 0:
        for i in range(gap, len(a)):
            value = a[i]
            j = i
            while j >= gap and a[j - gap] > value:
                a[j] = a[j - gap]
                j -= gap
            a[j] = value
        gap //= 2
    return a