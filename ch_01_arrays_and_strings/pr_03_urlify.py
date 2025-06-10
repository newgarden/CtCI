"""
Problem statement: Write a method to replace all spaces in a string with '%20'. You may assume that
the string has sufficient space at the end to hold the additional characters, and that you are
given the "true" length of the string. (Note: If implementing in Java, please use a character array
so that you can perform this operation in place.)

"""
import unittest


def urlify(st, true_len):
    """
    Solve the problem by modifying string in place in O(N) time.

    A list is used instead of a string, because Python strings are immutable.

    """
    space_count = 0
    for i in range(0, true_len):
        if st[i] == ' ':
            space_count += 1

    urlified_len = true_len + space_count * 2
    if len(st) > urlified_len:
        st[urlified_len:] = []

    i = true_len - 1
    j = len(st) - 1
    while i != j:
        if st[i] != ' ':
            st[j] = st[i]
            j -= 1
        else:
            st[j] = '0'
            st[j-1] = '2'
            st[j-2] = '%'
            j -= 3
        i -= 1

    return st


class Test(unittest.TestCase):
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13,
         list('Mr%20John%20Smith')),
        (list('StringWithoutSpaces'), 19,
         list('StringWithoutSpaces')),
        (list('String that is longer than needed              '), 33,
         list('String%20that%20is%20longer%20than%20needed'))
    ]

    def test_urlify(self):
        for d in self.data:
            self.assertEqual(urlify(d[0], d[1]), d[2])
