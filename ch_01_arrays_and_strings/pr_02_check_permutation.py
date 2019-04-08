# -*- coding: utf-8 -*-
"""
Problem statement: Given two strings, write a method to decide if one is a permutation of the
other.
"""
from collections import Counter
import unittest


def check_permutation(s1, s2):
    """
    Solve the problem in O(N) time, O(N) space.
    """
    if len(s1) != len(s2):
        return False
    counter = Counter()
    for ch in s1:
        counter[ch] += 1
    for ch in s2:
        counter[ch] -= 1
        if counter[ch] < 0:
            return False
    return True


class Test(unittest.TestCase):
    data_true = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    data_false = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def test_check_permutations(self):
        for data in self.data_true:
            self.assertTrue(check_permutation(*data))
        for data in self.data_false:
            self.assertFalse(check_permutation(*data))


if __name__ == '__main__':
    unittest.main()
