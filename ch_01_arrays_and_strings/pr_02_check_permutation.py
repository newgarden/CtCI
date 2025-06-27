"""Check Permutation.

Given two strings, write a method to decide if one is a permutation of the other.
"""
from collections import Counter
import unittest


def check_permutation(s1: str, s2: str) -> bool:
    """Check if s1 is a permutation of s2.

    Complexity: O(N) time, O(N) additional space.

    :param s1: First string.
    :param s2: Second string.

    :return: True if one string is a permutation of another.
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
