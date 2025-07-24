"""Sorted Merge.

You are given two sorted arrays, A and B, where A has a large enough buffer at the
end to hold B. Write a method to merge B into A in sorted order.
"""
import random
import unittest
from itertools import combinations_with_replacement


def merge_sorted(a: list, b: list) -> None:
    """Expand sorted list a and merge sorted list b into it in sorted order.

    Complexity: O(N) time, O(1) additional space.

    :param a: First sorted list.
    :param b: Second sorted list.
    """
    index_a = len(a) - 1
    index_b = len(b) - 1
    index_merged = len(a) + len(b) - 1
    a.extend([None for _ in range(len(b))])
    while index_a >= 0 and index_b >= 0:
        if a[index_a] >= b[index_b]:
            a[index_merged] = a[index_a]
            index_a -= 1
        else:
            a[index_merged] = b[index_b]
            index_b -= 1
        index_merged -= 1
    while index_b >= 0:
        a[index_merged] = b[index_b]
        index_b -= 1
        index_merged -= 1


class TestMergeSorted(unittest.TestCase):
    def generate_lists(self):
        for size in range(0, 6):
            if size <= 3:
                items = [-1, 0, 1]
            else:
                items = list(range(0 - size // 2, size - size // 2))
            for size_a in range(0, size + 1):
                size_b = size - size_a
                for a in combinations_with_replacement(items, size_a):
                    list_a = sorted(a)
                    for b in combinations_with_replacement(items, size_b):
                        list_b = sorted(b)
                        yield list_a, list_b, sorted(list_a + list_b)
        random.seed(739456)
        for size in range(6, 101):
            size_a = random.randint(0, size)
            size_b = size - size_a
            list_a = sorted([random.randint(-size // 2, size // 2) for _ in range(size_a)])
            list_b = sorted([random.randint(-size // 2, size // 2) for _ in range(size_b)])
            yield list_a, list_b, sorted(list_a + list_b)

    def test_merge_sorted(self):
        self.generate_lists()
        for a, b, merged in self.generate_lists():
            with self.subTest((a, b)):
                a_copy = a.copy()
                merge_sorted(a_copy, b)
                self.assertEqual(a_copy, merged)
