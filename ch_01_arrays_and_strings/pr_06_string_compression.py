# -*- coding: utf-8 -*-
"""
Problem statement: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).

"""
import unittest


def string_compression(st):
    """
    Solve the problem in O(N) time using O(N) additional space
    """
    if not st:
        return st

    compressed = [st[0]]
    count = 1
    for i in range(1, len(st)):
        if st[i] == compressed[-1]:
            count += 1
        else:
            compressed.append(str(count))
            compressed.append(st[i])
            count = 1
    compressed.append(str(count))

    if len(st) <= len(compressed):
        return st
    return ''.join(compressed)


class Test(unittest.TestCase):
    data = [
        ('', ''),
        ('a', 'a'),
        ('aa', 'aa'),
        ('aaa', 'a3'),
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef'),
        ('aabbbbc', 'a2b4c1'),
        ('aabcccdd', 'aabcccdd'),
        ('aAAAAbBBBBBcCC', 'a1A4b1B5c1C2'),
        ('aaAAbbBB', 'aaAAbbBB')
    ]

    def test_string_compression(self):
        for data in self.data:
            self.assertEqual(string_compression(data[0]), data[1])
