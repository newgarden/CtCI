# -*- coding: utf-8 -*-
"""
Intersection

Problem statement: Given two (singly) linked lists, determine if the two lists intersect. Return
the intersecting node. Note that the intersection is defined based on reference, not value. That is,
if the kth node of the first linked list is the exact same node (by reference) as the jth node of
the second linked list, then they are intersecting.

"""
import unittest
from linked_list import LinkedList


def get_intersection(lst1, lst2):
    """
    """
    len1 = 0
    node = lst1.head
    while node:
        len1 += 1
        node = node.next

    len2 = 0
    node = lst2.head
    while node:
        len2 += 1
        node = node.next

    runner1 = lst1.head
    runner2 = lst2.head
    if len2 > len1:
        for i in range(len2 - len1):
            runner2 = runner2.next
    elif len1 > len2:
        for i in range(len1 - len2):
            runner1 = runner1.next

    while runner1:
        if runner1 is runner2:
            return runner1
        runner1 = runner1.next
        runner2 = runner2.next

    return None


class TestIntersection(unittest.TestCase):
    data = [
        # (Head of the 1st list, Head of the 2nd list, Their common tail)
        ([], [], []),
        ([], [], [0]),
        ([0], [], []),
        ([0], [0], []),
        ([], [], [0, 1]),
        ([0], [], [1]),
        ([0], [0], [1]),
        ([0, 1], [], []),
        ([0, 1], [1], []),
        ([0, 1], [0, 1], []),
        ([], [], [0, 1, 2]),
        ([0], [], [1, 2]),
        ([0], [0], [1, 2]),
        ([0, 1], [], [2]),
        ([0, 1], [1], [2]),
        ([0, 1], [0, 1], [2]),
        ([0, 1, 2], [], []),
        ([0, 1, 2], [2], []),
        ([0, 1, 2], [1, 2], []),
        ([0, 1, 2], [0, 1, 2], []),
        ([], [], [0, 1, 2, 3]),
        ([0], [], [1, 2, 3]),
        ([0], [0], [1, 2, 3]),
        ([0, 1], [], [2, 3]),
        ([0, 1], [1], [2, 3]),
        ([0, 1], [0, 1], [2, 3]),
        ([0, 1, 2], [], [3]),
        ([0, 1, 2], [2], [3]),
        ([0, 1, 2], [1, 2], [3]),
        ([0, 1, 2], [0, 1, 2], [3]),
        ([0, 1, 2, 3], [], []),
        ([0, 1, 2, 3], [3], []),
        ([0, 1, 2, 3], [2, 3], []),
        ([0, 1, 2, 3], [1, 2, 3], []),
        ([0, 1, 2, 3], [0, 1, 2, 3], []),
        ([], [], [0, 1, 2, 3, 4]),
        ([0, 1], [], [2, 3, 4]),
        ([0, 1, 2], [], [3, 4]),
        ([0, 1, 2], [0, 1, 2], [3, 4]),
        ([0, 1, 2, 3], [2, 3], [4]),
        ([0, 1, 2, 3, 4], [], []),
        ([0, 1, 2, 3, 4], [2, 3, 4], []),
        ([0], [], [1, 2, 3, 4, 5]),
        ([0, 1], [1], [2, 3, 4, 5]),
        ([0, 1, 2], [2], [3, 4, 5]),
        ([0, 1, 2, 3], [], [4, 5]),
        ([0, 1, 2, 3], [1, 2, 3], [4, 5]),
        ([0, 1, 2, 3, 4], [4], [5]),
        ([0, 1, 2, 3, 4], [1, 2, 3, 4], [5]),
        ([0, 1, 2, 3, 4, 5], [], []),
        ([0, 1, 2, 3, 4, 5], [4, 5], []),
        ([0, 1, 2, 3, 4, 5], [2, 3, 4, 5], []),
        ([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], []),
        ([0], [0], [1, 2, 3, 4, 5, 6]),
        ([0, 1], [0, 1], [2, 3, 4, 5, 6]),
        ([0, 1, 2], [1, 2], [3, 4, 5, 6]),
        ([0, 1, 2, 3], [3], [4, 5, 6]),
        ([0, 1, 2, 3], [0, 1, 2, 3], [4, 5, 6]),
        ([0, 1, 2, 3, 4], [3, 4], [5, 6]),
        ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [5, 6]),
        ([0, 1, 2, 3, 4, 5], [5], [6]),
        ([0, 1, 2, 3, 4, 5], [3, 4, 5], [6]),
        ([0, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [6]),
        ([0, 1, 2, 3, 4, 5, 6], [], []),
        ([0, 1, 2, 3, 4, 5, 6], [5, 6], []),
        ([0, 1, 2, 3, 4, 5, 6], [3, 4, 5, 6], []),
        ([0, 1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], []),
    ]

    def test_get_intersection(self):
        for data in self.data:
            lst1 = LinkedList(data[0])
            lst2 = LinkedList(data[1])
            tail = LinkedList(data[2])

            if data[0]:
                lst1[len(data[0]) - 1].next = tail.head
            else:
                lst1.head = tail.head

            if data[1]:
                lst2[len(data[1]) - 1].next = tail.head
            else:
                lst2.head = tail.head

            self.assertIs(get_intersection(lst1, lst2), tail.head)
            self.assertIs(get_intersection(lst2, lst1), tail.head)

    def generate_test_data(self):
        max_list_len = 0
        for max_list_len in range(7):
            # print(max_list_len)
            for max_list_head_len in range(max_list_len + 1):
                tail_len = max_list_len - max_list_head_len
                head1 = [i for i in range(max_list_head_len)]
                tail = [i for i in range(max_list_head_len, max_list_len)]
                for min_list_head_len in range(max_list_head_len + 1):
                    head2 = [i for i in range(max_list_head_len - min_list_head_len, max_list_head_len)]
                    print('{},'.format((head1, head2, tail)))
