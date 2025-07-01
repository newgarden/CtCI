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


def merge_sort(lst: list) -> None:
    """Sort a list using merge sort algorithm.

    Complexity: O(N log N) time, O(N) additional space.

    :param lst: List to sort.
    """
    buffer = lst.copy()
    _merge_sort(lst, 0, len(lst) - 1, buffer)


def _merge_sort(lst: list, start: int, end: int, buffer: list) -> None:
    """Sort section of a list using merge sort.

    :param lst: List to sort.
    :param start: First index of the section.
    :param end: Last index of the section.
    :param buffer: Auxiliary buffer used during merge stage.
    """
    if end > start:
        middle = (start + end) // 2
        _merge_sort(lst, start, middle, buffer)
        _merge_sort(lst, middle + 1, end, buffer)
        _merge(lst, start, middle, end, buffer)


def _merge(lst: list, start: int, middle: int, end: int, buffer: list) -> None:
    """Merge two sorted adjacent sections of a list into one sorted section.

    :param lst: List to sort.
    :param start: First index of the left section.
    :param middle: Last index of the left section.
    :param end: Last index of the right section.
    :param buffer: Auxiliary buffer used during merge stage.
    """
    buffer[start:end + 1] = lst[start:end + 1]

    i = start
    i_left = start
    i_right = middle + 1
    while (i_left <= middle) and (i_right <= end):
        if buffer[i_left] <= buffer[i_right]:
            lst[i] = buffer[i_left]
            i_left += 1
        else:
            lst[i] = buffer[i_right]
            i_right += 1
        i += 1

    # If there are still some items in the left section, add them to the end.
    # If there are some items in the right section, don't touch them. They are already in place.
    if i_left <= middle:
        lst[i:end + 1] = buffer[i_left:middle + 1]


def quicksort(lst: list) -> None:
    """Sort a list using quicksort algorithm.

    Complexity: Time O(N log N) average case, O(N²) worst case. Additional space O(N log N) best case, O(N) worst case.

    :param lst: List to sort.
    """
    if len(lst) > 1:
        _quicksort(lst, 0, len(lst) - 1)


def _quicksort(lst: list, start: int, end: int) -> None:
    """Sort section of a list using quicksort.

    :param lst: List to sort.
    :param start: First index of the section.
    :param end: Last index of the section.
    """
    partition_index = _partition(lst, start, end)
    if start < partition_index - 1:
        _quicksort(lst, start, partition_index - 1)
    if end > partition_index:
        _quicksort(lst, partition_index, end)


def _partition(lst: list, start: int, end: int) -> int:
    """Partitioning part of quicksort.

    Split a list section into two partitions and swap items, so that all items of the left partition are smaller than
    all items of the right.

    :param lst: List to sort.
    :param start: First index of the section.
    :param end: Last index of the section.

    :return: First index of the right partition.
    """
    pivot = lst[(start + end) // 2]
    left = start
    right = end
    while left <= right:
        while lst[left] < pivot:
            left += 1
        while lst[right] > pivot:
            right -= 1
        if left <= right:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
    return left


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

    def test_merge_sort(self):
        for lst in self.generate_lists():
            with self.subTest(values=lst):
                lst_copy = lst.copy()
                sorted_list = sorted(lst)
                merge_sort(lst_copy)
                assert lst_copy == sorted_list

    def test_quicksort(self):
        for lst in self.generate_lists():
            with self.subTest(values=lst):
                lst_copy = lst.copy()
                sorted_list = sorted(lst)
                quicksort(lst_copy)
                assert lst_copy == sorted_list
