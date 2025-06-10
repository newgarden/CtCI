"""
Minimal Tree

Given a sorted (increasing order) array with unique integer elements, write an algorithm to create
a binary search tree with minimal height.

"""
import unittest

from .tree import BTree, BTreeNode


def minimal_tree(lst):
    """
    Build a binary search tree of minimal height from a sorted list.

    Args:
        lst (list): List sorted in increasing order.

    Returns:
        BTree: Binary search tree, where each node has left and right subtrees of equal weight or
            left subtree has one more node than the right subtree.

    """
    return BTree(recurse(lst, 0, len(lst) - 1))


def recurse(lst, start, end):
    """
    Build a binary search tree of minimal height from a portion of a sorted list.

    Internally used by minimal_tree() to recursively build the subtrees.

    Args:
        lst (list): List sorted in increasing order.
        start (int): Start index of the list portion.
        end (int): Last index of the list portion. Item with this index is included in the tree.

    Returns:
        BTreeNode: Root node of a subtree.

    """
    if start > end:
        return None

    if start == end:
        return BTreeNode(lst[start])

    middle = end - (end - start) // 2

    node = BTreeNode(lst[middle])
    node.left = recurse(lst, start, middle - 1)
    node.right = recurse(lst, middle + 1, end)

    return node


class TestMinimalTree(unittest.TestCase):
    data = [
        (0, []),
        (1, [0]),
        (2, [1, 0]),
        (3, [1, 0, 2]),
        (4, [2, 1, 3, 0]),
        (5, [2, 1, 4, 0, None, 3]),
        (6, [3, 1, 5, 0, 2, 4]),
        (7, [3, 1, 5, 0, 2, 4, 6]),
        (8, [4, 2, 6, 1, 3, 5, 7, 0]),
        (9, [4, 2, 7, 1, 3, 6, 8, 0, None, None, None, 5]),
        (10, [5, 2, 8, 1, 4, 7, 9, 0, None, 3, None, 6]),
        (11, [5, 2, 8, 1, 4, 7, 10, 0, None, 3, None, 6, None, 9]),
        (12, [6, 3, 9, 1, 5, 8, 11, 0, 2, 4, None, 7, None, 10]),
        (13, [6, 3, 10, 1, 5, 8, 12, 0, 2, 4, None, 7, 9, 11]),
        (14, [7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12]),
        (15, [7, 3, 11, 1, 5, 9, 13, 0, 2, 4, 6, 8, 10, 12, 14]),
        (19, [9, 4, 14, 2, 7, 12, 17, 1, 3, 6, 8, 11, 13, 16, 18, 0, None, None, None, 5, None,
              None, None, 10, None, None, None, 15]),
        (24, [12, 6, 18, 3, 9, 15, 21, 1, 5, 8, 11, 14, 17, 20, 23, 0, 2, 4, None, 7, None, 10,
              None, 13, None, 16, None, 19, None, 22]),
        (27, [13, 6, 20, 3, 10, 17, 24, 1, 5, 8, 12, 15, 19, 22, 26, 0, 2, 4, None, 7, 9, 11, None,
              14, 16, 18, None, 21, 23, 25]),
        (31, [15, 7, 23, 3, 11, 19, 27, 1, 5, 9, 13, 17, 21, 25, 29, 0, 2, 4, 6, 8, 10, 12, 14, 16,
              18, 20, 22, 24, 26, 28, 30])
    ]

    def test_minimal_tree(self):
        for array_len, serialized_tree in self.data:
            sorted_array = list(range(array_len))
            self.assertEqual(minimal_tree(sorted_array).as_list(), serialized_tree)
