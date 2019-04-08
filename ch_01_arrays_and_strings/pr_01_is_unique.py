# -*- coding: utf-8 -*-
"""
Problem statement: Implement an algorithm to determine if a string has all unique characters. What
if you cannot use additional data structures?
"""
import unittest


def is_unique(st):
    """
    Solve the problem in O(N) time using additional memory.
    """
    char_set = set()
    for ch in st:
        if ch in char_set:
            return False
        char_set.add(ch)
    return True


class Test(unittest.TestCase):
    unique = ['abcd', 's4fad']
    non_unique = ['23ds2', 'hb 627jh=j ()']

    def test_is_unique(self):
        for st in self.unique:
            self.assertTrue(is_unique(st))
        for st in self.non_unique:
            self.assertFalse(is_unique(st))


if __name__ == '__main__':
    unittest.main()
