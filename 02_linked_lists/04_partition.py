# -*- coding: utf-8 -*-
"""
Partition

Problem statement: Write code to partition a linked list around a value x, such that all nodes less
than x come before all nodes greater than or equal to x. If x is contained within the list, the
values of x only need to be after the elements less than x (see below). The partition element x can
appear anywhere in the "right partition"; it does not need to appear between the left and right
partitions.

Example:
    Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
    Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

"""
import unittest

from linked_list import LinkedList


def partition(lst, pivot):
    """
    Partition a list around a pivot value.

    Complexity: O(n) time, O(1) additional memory.

    This algorithm does not preserve relative order of elements. Partitioning is done by iterating
    through the list and moving nodes with value < pivot to the head of the list. In order to
    minimize permutations number, the movements are started after at least one node with value >
    pivot has been seen.

    Args:
        lst (LinkedList): List for partitioning.
        pivot: Pivot point.

    """
    if not lst.head:
        return
    node = lst.head
    while node.next:
        if node.next.value < pivot <= node.value:
            new_head = node.next
            node.next = node.next.next
            new_head.next = lst.head
            lst.head = new_head
        else:
            node = node.next


class TestPartition(unittest.TestCase):
    """
    Test partitioning function.

    This is a kind of a white box testing. It can verify that algorithm works exactly as it is
    described. But on the other hand it is not universal and cannot test partitioning implemented
    using a different algorithm.

    """
    data = [
        # (Input list, pivot, result list)
        ([], 5, []),
        ([1], 1, [1]),
        ([1, 3], 2, [1, 3]),
        ([3, 1], 2, [1, 3]),
        ([1, 2, 3], 2, [1, 2, 3]),
        ([3, 2, 1], 2, [1, 3, 2]),
        ([3, 2, 2], 2, [3, 2, 2]),
        ([3, 5, 8, 5, 10, 2, 1], 5, [1, 2, 3, 5, 8, 5, 10]),
        ([1, 3, 1, 3, 1, 3, 1, 2], 2, [1, 1, 1, 1, 3, 3, 3, 2]),
        ([6, 7, 8, 9, 1, 2, 3, 4], 5, [4, 3, 2, 1, 6, 7, 8, 9]),
        ([3, 9, 2, 2, 9, 3, 0, 5], 4, [0, 3, 2, 2, 3, 9, 9, 5]),
        ([1, 2, 3, 4, 5, 6, 7, 8], 10, [1, 2, 3, 4, 5, 6, 7, 8]),
        ([1, 2, 3, 4, 5, 6, 7, 8], 0, [1, 2, 3, 4, 5, 6, 7, 8]),
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, [1, 2, 3, 4, 5, 6, 7, 8]),
        ([-3, 1, -1, 2, -5, 7, -4, 4], 0, [-4, -5, -1, -3, 1, 2, 7, 4])
    ]

    def test_partition(self):
        for input_lst, pivot, output_lst in self.data:
            lst = LinkedList(input_lst)
            partition(lst, pivot)
            self.assertEqual(lst, LinkedList(output_lst))
