# -*- coding: utf-8 -*-
"""
Problem statement: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

"""
import unittest


def rotate_matrix(m):
    """
    Rotate matrix in place. Matrix may contain any objects, it is not necessary an image.
    """
    # We need to rotate n // 2 layers.
    n = len(m)
    for i in range(n // 2):
        l = i          # left border of the layer
        r = n - i - 1  # right border of the layer
        t = i          # top border of the layer
        b = n - i - 1  # bottom border of the layer
        for j in range(0, r - l):
            m[t][l + j], m[t + j][r], m[b][r - j], m[b - j][l] = \
                m[b - j][l], m[t][l + j], m[t + j][r], m[b][r - j]


class Test(unittest.TestCase):
    case0 = (
        [],
        []
    )
    case1 = (
        [['a']],
        [['a']]
    )
    case2 = (
        [['a', 'b'],
         ['c', 'd']],
        [['c', 'a'],
         ['d', 'b']]
    )
    case3 = (
        [['a', 'b', 'c'],
         ['d', 'e', 'f'],
         ['g', 'h', 'i']],
        [['g', 'd', 'a'],
         ['h', 'e', 'b'],
         ['i', 'f', 'c']],
    )
    case4 = (
        [['a', 'b', 'c', 'd'],
         ['e', 'f', 'g', 'h'],
         ['i', 'j', 'k', 'l'],
         ['m', 'n', 'o', 'p']],
        [['m', 'i', 'e', 'a'],
         ['n', 'j', 'f', 'b'],
         ['o', 'k', 'g', 'c'],
         ['p', 'l', 'h', 'd']],
    )
    case5 = (
        [['a', 'b', 'c', 'd', 'e'],
         ['f', 'g', 'h', 'i', 'j'],
         ['k', 'l', 'm', 'n', 'o'],
         ['p', 'q', 'r', 's', 't'],
         ['u', 'v', 'w', 'x', 'y']],
        [['u', 'p', 'k', 'f', 'a'],
         ['v', 'q', 'l', 'g', 'b'],
         ['w', 'r', 'm', 'h', 'c'],
         ['x', 's', 'n', 'i', 'd'],
         ['y', 't', 'o', 'j', 'e']]
    )
    case6 = (
        [['0', '1', '2', '3', '4', '5'],
         ['6', '7', '8', '9', 'a', 'b'],
         ['c', 'd', 'e', 'f', 'g', 'h'],
         ['i', 'j', 'k', 'l', 'm', 'o'],
         ['p', 'q', 'r', 's', 't', 'u'],
         ['v', 'w', 'x', 'y', 'z', '*']],
        [['v', 'p', 'i', 'c', '6', '0'],
         ['w', 'q', 'j', 'd', '7', '1'],
         ['x', 'r', 'k', 'e', '8', '2'],
         ['y', 's', 'l', 'f', '9', '3'],
         ['z', 't', 'm', 'g', 'a', '4'],
         ['*', 'u', 'o', 'h', 'b', '5']],
    )

    def test_rotate_matrix(self):
        cases = [self.case0, self.case1, self.case2, self.case3, self.case4, self.case5, self.case6]
        for case in cases:
            m = case[0]
            rotate_matrix(m)
            self.assertEqual(m, case[1])


if __name__ == '__main__':
    unittest.main()
