"""유닛 테스트 — 표준 라이브러리의 unittest만 쓴다.

실행: make test-py
"""

import sys
import unittest
from pathlib import Path

# src/를 import 경로에 넣는다. 패키지로 만들지 않아도 되도록.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sort import bubble_sort, insertion_sort, shell_sort  # noqa: E402


class TestBubbleSort(unittest.TestCase):
    def test_shuffled(self):
        a = [6, 8, 5, 9, 10, 1, 7, 2, 4, 3]
        self.assertEqual(bubble_sort(a), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_already_sorted(self):
        a = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(a), [1, 2, 3, 4, 5])

    def test_reversed(self):
        a = [5, 4, 3, 2, 1]
        self.assertEqual(bubble_sort(a), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        a = [3, 1, 3, 1, 2]
        self.assertEqual(bubble_sort(a), [1, 1, 2, 3, 3])

    def test_single(self):
        self.assertEqual(bubble_sort([42]), [42])

    def test_empty(self):
        self.assertEqual(bubble_sort([]), [])

    def test_sorts_in_place(self):
        a = [3, 1, 2]
        bubble_sort(a)
        self.assertEqual(a, [1, 2, 3])


class TestInsertionSort(unittest.TestCase):
    def test_cases(self):
        cases = [
            ([6, 8, 5, 9, 10, 1, 7, 2, 4, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([3, 1, 3, 1, 2], [1, 1, 2, 3, 3]),
            ([42], [42]),
            ([], []),
        ]
        for values, want in cases:
            with self.subTest(values=values):
                self.assertEqual(insertion_sort(values), want)

    def test_sorts_in_place(self):
        values = [3, 1, 2]
        insertion_sort(values)
        self.assertEqual(values, [1, 2, 3])


class TestShellSort(unittest.TestCase):
    def test_cases(self):
        cases = [
            ([6, 8, 5, 9, 10, 1, 7, 2, 4, 3], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([3, 1, 3, 1, 2], [1, 1, 2, 3, 3]),
            ([42], [42]),
            ([], []),
        ]
        for values, want in cases:
            with self.subTest(values=values):
                self.assertEqual(shell_sort(values), want)

    def test_sorts_in_place(self):
        values = [3, 1, 2]
        shell_sort(values)
        self.assertEqual(values, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
