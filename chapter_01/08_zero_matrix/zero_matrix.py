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

    def _read_from_file(self, f):
        """
        Read test cases from file

        The file contains multiple test cases. Each case has first line containing two integers M
        and N representing number of rows and columns in matrix. Next M lines contain rows of the
        input matrix followed by an empty line. After the empty line there are M lines containing
        rows of the expected output matrix followed by line filled with stars '*'. Starts are used
        to visually separate test cases.

        Each call to the method reads one test case.

        """
        line = f.readline()
        if not line:
            return None, None

        input = []
        output = []
        n_rows = int(line.split()[0])

        for row in range(n_rows):
            input.append([int(i) for i in f.readline().split()])
        f.readline()

        for row in range(n_rows):
            output.append([int(i) for i in f.readline().split()])
        f.readline()

        return input, output

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
        with open(self.TEST_DATA_FILE) as f:
            case = 1
            input, output = self._read_from_file(f)
            while input and output:
                with self.subTest(i=case):
                    zero_matrix(input)
                    self.assertEqual(input, output)
                    case += 1
                input, output = self._read_from_file(f)


if __name__ == '__main__':
    unittest.main()
