# -*- coding: utf-8 -*-
"""
Magic Index

A magic index in an array A[0 ... n - 1] is defined to be an index such that A[i] = i. Given a
sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.

"""
from itertools import chain, combinations
import unittest


def find_magic_index(s, start=None, end=None):
    """
    Find magic index in a sorted sequence of distinct integers.

    Sequence indexing is zero-based. If start and/or end indexes are provided function will search
    for magic index in slice s[start:end].

    Algorithm is based on recursive binary search. Complexity is O(log n) time and O(1) additional
    space.

    Args:
        s (sequence): Sorted sequence of distinct integers.
        start (int): Optional start index.
        end (int): Optional end index.

    Returns:
        int: Magic index or None.

    """
    if start is None:
        start = 0
    if end is None:
        end = len(s)
    if end <= start or start < 0 or end <= 0:
        return

    mid_index = (start + end) // 2

    if s[mid_index] == mid_index:
        return mid_index
    elif s[mid_index] < mid_index:
        return find_magic_index(s, mid_index + 1, end)
    else:
        return find_magic_index(s, start, mid_index)


class TestFindMagicIndex(unittest.TestCase):
    """
    Test find_magic_index() function.
    """

    def test_empty(self):
        """
        Test empty sequence.
        """
        self.assertIs(find_magic_index([]), None)

    def test_1(self):
        """
        Test sequence with a single element.
        """
        self.assertEqual(find_magic_index([-2]), None)
        self.assertEqual(find_magic_index([-1]), None)
        self.assertEqual(find_magic_index([0]), 0)
        self.assertEqual(find_magic_index([1]), None)
        self.assertEqual(find_magic_index([2]), None)

    def test_2_3(self):
        """
        Test sequences with 2 and 3 elements.

        For 2-element sequences test cases are generated as all possible combinations of integers
        in range -2...2 inclusively. For 3-element sequences test cases are generated as all
        possible combinations of integers in range -3...3 inclusively.

        """
        for data in chain(combinations(range(-2, 3), 2), combinations(range(-3, 4), 3)):
            magic_index = find_magic_index(data)
            if magic_index is not None:
                self.assertEqual(magic_index, data[magic_index])
            else:
                for i, value in enumerate(data):
                    self.assertNotEqual(i, value)

    def test_large(self):
        """
        Test sequences of larger length.
        """
        positive_cases = [
            # odd length
            (-1, 0, 1, 2, 4),
            (-1, 0, 1, 3, 5, 7, 9),
            (-3, -1, 0, 3, 4, 5, 7, 9, 11),
            (0, 1, 4, 5, 6, 8, 9, 11, 12, 15, 16),
            (-6, -5, -3, -1, 0, 3, 5, 7, 9, 10, 11, 12, 13),
            (-11, -3, -1, 0, 2, 3, 6, 9, 10, 11, 13, 16, 20, 21, 30),
            (-8, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 8, 9, 10, 12, 15, 17),
            (-7, -6, -5, -4, -1, 0, 2, 3, 6, 7, 8, 10, 12, 13, 14, 15, 16, 19, 20),
            (-10, -4, -3, -1, 0, 1, 2, 4, 6, 7, 10, 12, 14, 16, 17, 19, 23, 25, 30, 40, 41),
            (0, 2, 5, 6, 8, 11, 13, 18, 21, 27, 31, 38, 46, 49, 52, 55, 58, 71, 84, 96, 97, 98, 99),

            # even length
            (0, 2, 4, 5, 7, 8),
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9),
            (-5, -3, -1, 0, 1, 3, 6, 7, 8, 9, 10, 11),
            (-3, -2, 0, 1, 4, 7, 9, 10, 12, 13, 14, 15, 20, 21),
            (-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 10, 15, 16, 17, 18, 19, 20, 21),
            (-4, -3, -1, 0, 2, 3, 4, 5, 7, 8, 9, 11, 13, 14, 16, 18, 19, 20, 21, 23),
            (-3, -1, 0, 1, 2, 5, 6, 9, 10, 11, 12, 14, 15, 17, 20, 21, 23, 24, 25, 26, 27, 28),
            (-1, 1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
             27),
            (-9, -8, -6, -4, -2, -1, 0, 1, 3, 4, 6, 7, 9, 10, 11, 13, 14, 17, 18, 19, 20, 23, 25,
             26, 28, 30),
            (-15, -13, -11, -9, -8, -6, -4, -3, -1, 0, 3, 4, 5, 7, 8, 9, 11, 12, 13, 15, 18, 19,
             20, 23, 25, 27, 30, 31),
            (-3, -2, 0, 1, 2, 5, 8, 9, 10, 11, 13, 14, 15, 16, 18, 19, 20, 22, 23, 24, 27, 29, 40,
             42, 43, 45, 47, 48, 50, 55),

            # length 2^n
            (-1, 1, 3, 5),
            (-2, 1, 3, 4, 8, 11, 13, 15),
            (-8, -3, -2, -1, 0, 3, 5, 7),
            (-7, -6, -5, 0, 1, 2, 5, 6, 8, 10, 12, 13, 15, 20, 21, 22),
            (-3, -2, -1, 0, 3, 5, 7, 8, 10, 11, 12, 18, 19, 20, 22, 23),
            (-8, -5, -3, -2, 0, 1, 2, 3, 4, 6, 8, 9, 10, 11, 13, 15),
            (0, 2, 3, 5, 7, 8, 11, 12, 14, 15, 21, 23, 28, 29, 32, 34, 35, 36, 40, 41, 45, 48, 50,
             53, 56, 58, 60, 61, 62, 63, 64, 70),
            (-30, -20, -15, -12, -11, -10, -7, -6, -4, -3, -2, -1, 0, 2, 2, 4, 5, 6, 7, 9, 10, 11,
             15, 17, 19, 20, 21, 23, 25, 28, 30, 35)
        ]
        for data in positive_cases:
            magic_index = find_magic_index(data)
            self.assertEqual(magic_index, data[magic_index])

        negative_cases = [
            # odd length
            (1, 2, 3, 4, 5),
            (1, 2, 3, 5, 7, 11, 13, 17, 19),
            (-13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1),
            (-19, -17, -15, -11, -9, -4, -2, 0, 1, 3, 5, 6, 7, 10, 12, 14, 17),
            (-9, -5, -3, -1, 0, 2, 4, 8, 9, 10, 11, 12, 15, 17, 21, 22, 24, 25, 28, 30, 31),

            # even length
            (5, 6, 7, 8, 9, 10),
            (1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233),
            (-18, -16, -14, -12, -10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16),
            (-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22),
            (-13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 22, 23, 24, 25, 26, 27, 28,
             29, 30, 31, 32, 33, 34),
            (-9, -7, -4, -3, -2, -1, 0, 1, 3, 6, 7, 8, 10, 12, 15, 16, 17, 18, 19, 21, 23, 24, 26,
             31, 35, 38, 40, 45, 48, 50),

            # length 2^n
            (-5, -2, 0, 2),
            (4, 5, 8, 13, 15, 17, 20, 21),
            (-1, 0, 1, 2, 5, 6, 7, 9, 11, 12, 14, 15, 16, 17, 19, 20),
            (-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6,
             7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        ]
        for data in negative_cases:
            self.assertIs(find_magic_index(data), None)
