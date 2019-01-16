# -*- coding: utf-8 -*-
"""
Robot in a Grid

Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can
only move in two directions, right and down, but certain cells are "off limits" such that the robot
cannot step on them. Design an algorithm to find a path for the robot from the top left to the
bottom right.

Problem depiction and test cases: ./images/problem-2-robot-in-a-grid.svg

"""
import unittest


def find_path(rows, cols, off_limits):
    """
    Find path from the top left to the bottom right corner of the grid.

    Search is done using bottom-up dynamic programming in O(rows * cols) time and O(rows * cols)
    additional space.

    The algorithm is deterministic. Robot always prefers to go down first turning to the right only
    when there is no way by going down.

    Args:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid
        off_limits (list): List of "off limits" cells. Cells are represented as coordinate tuples
            in the form (row, column) with zero-based indexes.

    Returns:
        list: Path from the top left corner to the bottom right or empty list if there is no path.
            Like off_limits argument the path is represented as a list of coordinates.

    """
    if not (rows > 0 and cols > 0):
        return []

    off_limits = set(off_limits)

    last_row = rows - 1  # Index of the last row
    last_col = cols - 1  # Index of the last column

    if (last_row, last_col) in off_limits:
        return []

    no_way = 0  # Marker for cells from which the bottom right cell is unreachable
    down = 1    # Marker for cells from which the bottom right cell can be reached by going down
    right = 2   # Marker for cells from which the bottom right cell can be reached by going right
    finish = 3  # Marker for the bottom right cell

    # Path matrix with cells that will be marked with one of the direction markers.
    path_matrix = [[no_way] * cols for i in range(rows)]
    path_matrix[last_row][last_col] = finish

    for r in range(last_row, -1, -1):
        for c in range(last_col, -1, -1):
            if (r, c) in off_limits:
                continue
            if r < last_row and path_matrix[r + 1][c]:
                path_matrix[r][c] = down
                continue
            if c < last_col and path_matrix[r][c + 1]:
                path_matrix[r][c] = right

    if path_matrix[0][0] == no_way:
        return []

    # Build the resulting path by following the direction markers.
    # Path always has length row + cols - 1.
    path = []
    r, c = 0, 0
    while len(path) < rows + cols - 1:
        path.append((r, c))
        if path_matrix[r][c] == down:
            r += 1
        else:
            c += 1

    return path


class TestFindPath(unittest.TestCase):
    data = [
        (0, 0, [], []),
        (1, 1, [], [(0, 0)]),
        (1, 1, [(0, 0)], []),
        (1, 2, [], [(0, 0), (0, 1)]),
        (1, 2, [(0, 0)], []),
        (1, 2, [(0, 1)], []),
        (1, 2, [(0, 0), (0, 1)], []),
        (2, 1, [], [(0, 0), (1, 0)]),
        (2, 1, [(0, 0)], []),
        (2, 1, [(1, 0)], []),
        (2, 1, [(0, 0), (1, 0)], []),
        (2, 2, [], [(0, 0), (1, 0), (1, 1)]),
        (2, 2, [(0, 0)], []),
        (2, 2, [(0, 1)], [(0, 0), (1, 0), (1, 1)]),
        (2, 2, [(1, 0)], [(0, 0), (0, 1), (1, 1)]),
        (2, 2, [(1, 1)], []),
        (2, 2, [(0, 1), (1, 0)], []),
        (2, 2, [(0, 1), (1, 1)], []),
        (2, 3, [], [(0, 0), (1, 0), (1, 1), (1, 2)]),
        (2, 3, [(1, 0)], [(0, 0), (0, 1), (1, 1), (1, 2)]),
        (2, 3, [(1, 1)], [(0, 0), (0, 1), (0, 2), (1, 2)]),
        (2, 3, [(0, 1), (1, 1)], []),
        (2, 3, [(1, 2)], []),
        (3, 2, [], [(0, 0), (1, 0), (2, 0), (2, 1)]),
        (3, 2, [(1, 0)], [(0, 0), (0, 1), (1, 1), (2, 1)]),
        (3, 2, [(2, 0)], [(0, 0), (1, 0), (1, 1), (2, 1)]),
        (3, 2, [(1, 1)], [(0, 0), (1, 0), (2, 0), (2, 1)]),
        (3, 2, [(1, 0), (1, 1)], []),
        (3, 2, [(1, 0), (2, 0)], [(0, 0), (0, 1), (1, 1), (2, 1)]),
        (3, 2, [(1, 1), (2, 0)], []),
        (3, 3, [], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
        (3, 3, [(0, 0)], []),
        (3, 3, [(1, 0)], [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]),
        (3, 3, [(1, 1)], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
        (3, 3, [(2, 1)], [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]),
        (3, 3, [(0, 1), (1, 0)], []),
        (3, 3, [(1, 0), (1, 2)], [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]),
        (3, 3, [(1, 2), (2, 1)], []),
        (3, 3, [(1, 0), (2, 1)], [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]),
        (3, 3, [(1, 0), (1, 1), (1, 2)], []),
        (3, 3, [(1, 0), (1, 1), (2, 1)], [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]),
        (3, 3, [(1, 0), (1, 2), (2, 1)], []),
        (3, 3, [(0, 1), (2, 0), (2, 1)], [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]),
        (3, 3, [(0, 1), (0, 2), (1, 2), (2, 0)], [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2)]),
        (3, 3, [(0, 1), (0, 2), (1, 1), (2, 0)], []),
        (2, 4, [(1, 1)], [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)]),
        (2, 4, [(0, 2), (1, 1)], []),
        (2, 4, [(0, 3), (1, 1)], [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3)]),
        (2, 4, [(0, 0), (1, 3)], []),
        (3, 4, [(1, 2), (2, 0), (2, 2)], [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3)]),
        (3, 4, [(0, 3), (2, 0)], [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3)]),
        (3, 4, [(0, 2), (1, 1), (2, 2)], []),
        (3, 4, [(1, 1), (2, 2)], [(0, 0), (0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]),
        (4, 2, [(0, 1), (1, 1), (3, 0)], [(0, 0), (1, 0), (2, 0), (2, 1), (3, 1)]),
        (4, 2, [(1, 1), (2, 0)], []),
        (4, 2, [(0, 1), (2, 1)], [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1)]),
        (4, 3, [(2, 1), (3, 0)], [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2), (3, 2)]),
        (4, 3, [(1, 1), (1, 2), (3, 1)], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2)]),
        (4, 3, [(1, 1), (2, 1), (2, 2), (3, 0)], []),
        (4, 4, [(3, 3)], []),
        (4, 4, [(1, 0), (1, 3), (2, 1)], [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3)]),
        (4, 4, [(2, 2), (2, 3), (3, 2)], []),
        (4, 4, [(0, 1), (2, 0), (2, 2), (3, 2)],
         [(0, 0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]),
        (4, 4, [(1, 2), (1, 3), (2, 1), (3, 0), (3, 1)], []),
        (4, 4, [(1, 0), (1, 1), (2, 1), (2, 3)],
         [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (3, 3)]),
        (4, 4, [(1, 0), (2, 1), (3, 2)], [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (2, 3), (3, 3)]),
        (4, 4, [(0, 2), (0, 3), (1, 0), (1, 2), (1, 3), (2, 0), (3, 0), (3, 1), (3, 2)],
         [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (2, 3), (3, 3)]),
        (1, 5, [], [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)]),
        (1, 5, [(0, 2)], []),
        (1, 5, [(0, 0)], []),
        (3, 5, [(0, 3), (1, 2), (1, 4), (2, 0)],
         [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (2, 3), (2, 4)]),
        (3, 5, [(0, 4), (1, 1), (1, 3), (2, 1)],
         [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 3), (2, 4)]),
        (3, 5, [(0, 3), (1, 2), (2, 1)], []),
        (5, 1, [], [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]),
        (5, 1, [(1, 0), (3, 0)], []),
        (5, 2, [], [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1)]),
        (5, 2, [(2, 0), (3, 0), (4, 0)], [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (4, 1)]),
        (5, 2, [(0, 1), (2, 1), (4, 0)], [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1)]),
        (5, 2, [(1, 1), (2, 0)], []),
        (5, 3, [(1, 1), (3, 1), (4, 1)], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2)]),
        (5, 5, [(0, 4), (1, 3), (3, 1), (3, 3), (4, 0)],
         [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]),
        (5, 5, [(1, 1), (1, 3), (3, 1), (3, 3), (4, 0), (4, 2)],
         [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (4, 4)]),
        (5, 5, [(0, 2), (1, 1), (1, 3), (2, 3), (3, 1), (3, 2), (3, 3), (4, 0), (4, 1)], []),
        (5, 5, [(1, 0), (1, 2), (1, 4), (2, 2), (3, 1), (3, 2), (3, 3)],
         [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 4), (3, 4), (4, 4)]),
        (5, 5, [(1, 0), (1, 1), (3, 2), (3, 3), (3, 4)], []),
        (5, 5, [(1, 0), (1, 2), (1, 4), (3, 1), (3, 3)],
         [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4)]),
        (6, 6, [(1, 0), (1, 2), (1, 4), (3, 1), (3, 3), (3, 5), (5, 0), (5, 2), (5, 4)],
         [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2), (3, 2), (4, 2), (4, 3), (4, 4), (4, 5), (5, 5)]),
        (6, 6, [(0, 4), (1, 2), (2, 2), (2, 4), (3, 0), (3, 1), (3, 2), (4, 4), (4, 5)],
         [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (5, 4), (5, 5)]),
        (6, 6, [(1, 0), (1, 2), (1, 3), (2, 2), (2, 4), (3, 1), (3, 2), (4, 4), (4, 5)], []),
        (6, 6, [(0, 1), (0, 3), (0, 5), (2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5)],
         [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)]),
        (6, 6, [(1, 1), (2, 0), (2, 3), (3, 2), (3, 5), (4, 4)], []),
        (6, 6, [(1, 1), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 0), (4, 1), (4, 3),(4, 4)],
         [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (4, 2), (5, 2), (5, 3), (5, 4), (5, 5)])
    ]

    def test_find_path(self):
        for rows, cols, off_limits, result in self.data:
            self.assertEqual(find_path(rows, cols, off_limits), result)
