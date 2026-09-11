import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from shell_sort import shell_sort  # noqa: E402


class TestShellSort(unittest.TestCase):
    def test_shuffled(self):
        values = [6, 8, 5, 9, 10, 1, 7, 2, 4, 3]
        self.assertEqual(shell_sort(values), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_sorts_in_place(self):
        values = [3, 1, 2]
        result = shell_sort(values)
        self.assertIs(result, values)

    def test_duplicates(self):
        self.assertEqual(shell_sort([3, 1, 3, 1, 2]), [1, 1, 2, 3, 3])

    def test_single(self):
        self.assertEqual(shell_sort([42]), [42])


if __name__ == "__main__":
    unittest.main()