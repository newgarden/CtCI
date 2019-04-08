# -*- coding: utf-8 -*-
"""
Zero matrix.

Problem statement: Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0.

"""
from copy import deepcopy
import unittest


def zero_matrix(matrix):
    """
    Modify matrix in place in O(MxN) time and O(1) additional space.
    """
    if not matrix:
        return

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    # First row and first column of the matrix are used to store row and columns to nullify.
    # At the beginning we determine if the first row and/or first column contain a zero.
    first_row_zero = False
    first_col_zero = False
    for col in range(n_cols):
        if not matrix[0][col]:
            first_row_zero = True
            break
    for row in range(n_rows):
        if not matrix[row][0]:
            first_col_zero = True
            break

    # Then go through the rest of the matrix and determine which rows and columns must be zeroed.
    for row in range(1, n_rows):
        for col in range(1, n_cols):
            if not matrix[row][col]:
                matrix[0][col] = 0
                matrix[row][0] = 0

    # Go through the rest of the matrix again and insert zeros where needed.
    for row in range(1, n_rows):
        for col in range(1, n_cols):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0

    # Nullify first row and column if needed.
    if first_row_zero:
        for col in range(n_cols):
            matrix[0][col] = 0
    if first_col_zero:
        for row in range(n_rows):
            matrix[row][0] = 0


class Test(unittest.TestCase):
    data = [
        # empty
        ([], []),

        # 1x1
        ([[0]], [[0]]),

        ([[1]], [[1]]),

        # 1x4
        ([[1, 2, 3, 4]],
         [[1, 2, 3, 4]]),

        # 1x5
        ([[1, 2, 0, 3, 4]],
         [[0, 0, 0, 0, 0]]),

        # 1x6
        ([[0, 1, 2, 3, 4, 5]],
         [[0, 0, 0, 0, 0, 0]]),

        # 3x1
        ([[1], [2], [3]],
         [[1], [2], [3]]),

        # 4x1
        ([[0], [1], [2], [3]],
         [[0], [0], [0], [0]]),

        # 5x1
        ([[1], [2], [3], [4], [0]],
         [[0], [0], [0], [0], [0]]),

        # 2x2
        ([[1, 2],
          [3, 4]],
         [[1, 2],
          [3, 4]]),

        ([[0, 2],
          [3, 4]],
         [[0, 0],
          [0, 4]]),

        ([[1, 2],
          [0, 4]],
         [[0, 2],
          [0, 0]]),

        ([[1, 2],
          [3, 0]],
         [[1, 0],
          [0, 0]]),

        ([[1, 0],
          [3, 4]],
         [[0, 0],
          [3, 0]]),

        # 3x5
        ([[1, 2, 3, 4, 5],
          [6, 7, 0, 9, 1],
          [2, 3, 4, 5, 6]],

         [[1, 2, 0, 4, 5],
          [0, 0, 0, 0, 0],
          [2, 3, 0, 5, 6]]),

        # 4x4
        ([[1, 2, 3, 4],
          [5, 6, 7, 8],
          [0, 1, 2, 3],
          [4, 5, 6, 7]],

         [[0, 2, 3, 4],
          [0, 6, 7, 8],
          [0, 0, 0, 0],
          [0, 5, 6, 7]]),

        ([[1, 2, 0, 4],
          [5, 6, 7, 8],
          [9, 1, 2, 3],
          [4, 5, 6, 7]],

         [[0, 0, 0, 0],
          [5, 6, 0, 8],
          [9, 1, 0, 3],
          [4, 5, 0, 7]]),

        # 5x4
        ([[0, 1, 2, 3],
          [4, 5, 6, 7],
          [8, 9, 1, 2],
          [3, 4, 5, 6],
          [7, 8, 9, 1]],

         [[0, 0, 0, 0],
          [0, 5, 6, 7],
          [0, 9, 1, 2],
          [0, 4, 5, 6],
          [0, 8, 9, 1]]),

        # 5x5
        ([[1, 1, 1, 1, 1],
          [1, 0, 1, 0, 1],
          [1, 1, 1, 1, 1],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 1, 1]],

         [[1, 0, 1, 0, 1],
          [0, 0, 0, 0, 0],
          [1, 0, 1, 0, 1],
          [0, 0, 0, 0, 0],
          [1, 0, 1, 0, 1]]),

        # 6x6
        ([[1, 2, 3, 4, 5, 6],
          [7, 8, 9, 0, 1, 2],
          [3, 4, 5, 6, 7, 8],
          [9, 0, 1, 2, 3, 4],
          [5, 6, 7, 8, 9, 0],
          [1, 2, 3, 4, 5, 6]],

         [[1, 0, 3, 0, 5, 0],
          [0, 0, 0, 0, 0, 0],
          [3, 0, 5, 0, 7, 0],
          [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0],
          [1, 0, 3, 0, 5, 0]]),

        # 7x7
        ([[1, 2, 3, 4, 5, 6, 0],
          [8, 9, 1, 2, 3, 4, 5],
          [6, 7, 8, 9, 1, 2, 3],
          [4, 5, 6, 0, 8, 9, 1],
          [2, 3, 4, 5, 6, 7, 8],
          [9, 1, 2, 3, 4, 5, 6],
          [0, 8, 9, 1, 2, 3, 4]],

         [[0, 0, 0, 0, 0, 0, 0],
          [0, 9, 1, 0, 3, 4, 0],
          [0, 7, 8, 0, 1, 2, 0],
          [0, 0, 0, 0, 0, 0, 0],
          [0, 3, 4, 0, 6, 7, 0],
          [0, 1, 2, 0, 4, 5, 0],
          [0, 0, 0, 0, 0, 0, 0]])
    ]

    def test_zero_matrix(self):
        for test_input, expected_result in self.data:
            input_copy = deepcopy(test_input)
            zero_matrix(input_copy)
            self.assertEqual(input_copy, expected_result)


if __name__ == '__main__':
    unittest.main()
