"""
Implementations of some well-known sorting algorithms.
"""
from itertools import combinations_with_replacement, permutations
from random import randint
import unittest


def bubble_sort(lst):
    """
    Sort a list using bubble sort algorithm.

    Complexity: Time O(N²) worst case, O(N) best case; O(1) additional space.

    Attributes:
        lst (list): List to sort.

    """
    for i in range(len(lst) - 1, 0, -1):
        swap = False
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swap = True
        if not swap:
            break


def selection_sort(lst):
    """
    Sort a list using selection sort algorithm.

    Complexity: O(N²) time, O(1) additional space.

    Attributes:
        lst (list): List to sort.

    """
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                lst[i], lst[j] = lst[j], lst[i]


class TestSorting(unittest.TestCase):

    def generate_lists(self):
        """
        Generate test lists for sorting.

        First generate lists with lengths ranging from 0 to 4 with all possible combinations and permutations of the
        items.

        Next generate lists with lengths ranging from 5 to 50 containing random items. For each length three lists are
        generated: unsorted, sorted ascending, sorted descending.

        Yields:
            list: List for test.

        """
        for i in range(5):
            values = list(range(i))
            for combination in combinations_with_replacement(values, i):
                unique_permutations = set()
                for permutation in permutations(combination):
                    if permutation not in unique_permutations:
                        unique_permutations.add(permutation)
                        yield list(permutation)

        for i in range(5, 51):
            lst = []
            for _ in range(0, i):
                lst.append(randint(-10, 10))
            yield lst
            lst.sort()
            yield lst
            lst.reverse()
            yield lst

    def test_bubble_sort(self):
        for lst in self.generate_lists():
            with self.subTest(values=lst):
                lst_copy = lst.copy()
                sorted_list = sorted(lst)
                bubble_sort(lst_copy)
                assert lst_copy == sorted_list

    def test_selection_sort(self):
        for lst in self.generate_lists():
            with self.subTest(values=lst):
                lst_copy = lst.copy()
                sorted_list = sorted(lst)
                selection_sort(lst_copy)
                assert lst_copy == sorted_list
