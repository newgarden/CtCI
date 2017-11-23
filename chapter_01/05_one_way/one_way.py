# -*- coding: utf-8 -*-
"""
Problem statement: There are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings, write a function to check
if they are one edit (or zero edits) away.

"""
import unittest


def one_way(s1, s2):
    """
    Solve the problem in a single pass in O(N) time without additional memory.
    """
    if abs(len(s1) - len(s2)) > 1:
        return False

    i, j, diff_count = 0, 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            diff_count += 1
            if diff_count > 1:
                return False
            if len(s1) > len(s2):
                i += 1
            elif len(s2) > len(s1):
                j += 1
            else:
                i += 1
                j += 1
        else:
            i += 1
            j += 1

    return True


class Test(unittest.TestCase):
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('ple', 'pale', True),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False),
        ('aaa', 'faad', False)
    ]

    def test_one_way(self):
        for data in self.data:
            self.assertEqual(one_way(data[0], data[1]), data[2])


if __name__ == '__name__':
    unittest.main()
