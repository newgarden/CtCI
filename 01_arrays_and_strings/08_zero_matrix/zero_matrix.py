# -*- coding: utf-8 -*-
"""
Zero matrix.

Problem statement: Write an algorithm such that if an element in an MxN matrix is 0, its entire row
and column are set to 0.

"""
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
    TEST_DATA_FILE = 'test_data.txt'

    def _test_cases(self):
        """
        Returns iterator to read test cases from file one by one.

        The file contains multiple test cases. Each case has first line containing two integers M
        and N representing number of rows and columns in matrix. Next M lines contain rows of the
        input matrix followed by an empty line. After the empty line there are M lines containing
        rows of the expected output matrix followed by line filled with stars '*'. Starts are used
        to visually separate test cases.

        """
        with open(self.TEST_DATA_FILE) as f:
            line = f.readline()
            while line:
                data_in = []
                data_out = []
                n_rows = int(line.split()[0])

                for row in range(n_rows):
                    data_in.append([int(i) for i in f.readline().split()])
                f.readline()

                for row in range(n_rows):
                    data_out.append([int(i) for i in f.readline().split()])
                f.readline()

                yield data_in, data_out
                line = f.readline()

    def test_empty(self):
        """
        Test function with empty input.
        """
        matrix = []
        zero_matrix(matrix)
        self.assertEqual(matrix, [])

    def test_one_element(self):
        """
        Test function in edge case when matrix contains one row and one column.
        """
        matrix = [[1]]
        zero_matrix(matrix)
        self.assertEqual(matrix, [[1]])

        matrix = [[0]]
        zero_matrix(matrix)
        self.assertEqual(matrix, [[0]])

    def test_zero_matrix(self):
        """
        Test function in more sophisticated cases taken from file.
        """
        case = 1
        for data_in, data_out in self._test_cases():
            with self.subTest(i=case):
                zero_matrix(data_in)
                self.assertEqual(data_in, data_out)
                case += 1


if __name__ == '__main__':
    unittest.main()
