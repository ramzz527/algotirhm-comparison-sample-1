import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from insertion_sort import insertion_sort  # noqa: E402


class TestInsertionSort(unittest.TestCase):
    def test_shuffled(self):
        values = [6, 8, 5, 9, 10, 1, 7, 2, 4, 3]
        self.assertEqual(insertion_sort(values), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_sorts_in_place(self):
        values = [3, 1, 2]
        result = insertion_sort(values)
        self.assertIs(result, values)

    def test_reversed(self):
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_empty(self):
        self.assertEqual(insertion_sort([]), [])


if __name__ == "__main__":
    unittest.main()