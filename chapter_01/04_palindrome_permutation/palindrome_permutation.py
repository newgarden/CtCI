# -*- coding: utf-8 -*-
"""
Problem statement: Given a string, write a function to check if it is a permutation of a
palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

"""
import unittest


def palindrome_permutation(st):
    """
    Solves the problem in O(N) time, O(N) space.
    """
    char_set = set()
    for ch in st:
        if ch.isalnum():
            if ch.lower() in char_set:
                char_set.remove(ch.lower())
            else:
                char_set.add(ch.lower())
    return len(char_set) <= 1


class Test(unittest.TestCase):
    data = [
        ('', True),
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True),
        ('нагнеантиА аримтгнер ', True),
        ('Это не палиндром', False),
        ('404', True),
        ('123', False),
        ('AbB1122', True)
    ]

    def test_palindrome_permutation(self):
        for data in self.data:
            self.assertEqual(palindrome_permutation(data[0]), data[1])


if __name__ == '__main__':
    unittest.main()
