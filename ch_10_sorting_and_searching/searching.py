"""Binary search implementation examples."""
import unittest
from random import randint
from typing import Any


def binary_search(lst: list, value: Any) -> int | None:
    """Find a value in a sorted list using binary search.

    Complexity: O(log N) time, O(1) additional space.

    :param lst: Sorted list.
    :param value: Value to search in the list.

    :return: Index of the value in the list. None if the value is not found in the list.
    """
    start = 0
    end = len(lst) - 1
    while end >= start:
        middle = (start + end) // 2
        if lst[middle] > value:
            end = middle - 1
        elif lst[middle] < value:
            start = middle + 1
        else:
            return middle
    return None


class TestSearching(unittest.TestCase):

    def generate_lists(self):
        for size in range(1, 50):
            # For each size generate two lists. One with many repetitions, another with fewer repetitions.
            lst_1 = []
            lst_2 = []
            for i in range(size):
                lst_1.append(randint(-10, 10))
                lst_2.append(randint(-150, 150))
            lst_1.sort()
            lst_2.sort()
            yield lst_1
            yield lst_2

    def test_binary_search(self):
        with self.subTest(([], 1)):
            self.assertIsNone(binary_search([], 1))

        for lst in self.generate_lists():
            for value in lst:
                with self.subTest((lst, value)):
                    index = binary_search(lst, value)
                    self.assertEqual(lst[index], value)

            for i in range(len(lst) - 1):
                value = (lst[i] + lst[i+1]) // 2
                if value != lst[i] and value != lst[i + 1]:
                    with self.subTest((lst, value)):
                        self.assertIsNone(binary_search(lst, value))

            if lst:
                with self.subTest((lst, lst[0] - 1)):
                    self.assertIsNone(binary_search(lst, lst[0] - 1))
                with self.subTest((lst, lst[-1] + 1)):
                    self.assertIsNone(binary_search(lst, lst[-1] + 1))
