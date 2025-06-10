"""
String Rotation

Problem statement: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only
one call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat").

"""
import unittest


def string_rotation(s1, s2):
    """
    Check if s2 is a rotation of s1.

    Takes O(N+M) time and O(N) additional space, where N and M are lengths of s1 and s2.
    Operator "in" is used as a substitute for isSubstring. This problem may be solved in O(1) space
    without isSubstring, but use of this function is dictated by the problem statement.

    """
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)


class Test(unittest.TestCase):
    data = [
        ('', '', True),
        ('abc', '', False),
        ('', 'spam', False),
        ('abcde', 'abcde', True),
        ('waterbottle', 'erbottlewat', True),
        ('waterbottle', 'elttobretaw', False),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False),
        ('aaaa', 'aaaa', True),
        ('aaaa', 'aaa', False),
        ('racecar', 'carrace', True)
    ]

    def test_string_rotation(self):
        for data in self.data:
            self.assertEqual(string_rotation(data[0], data[1]), data[2])
