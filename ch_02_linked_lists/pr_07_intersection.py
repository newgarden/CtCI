"""
Intersection

Problem statement: Given two (singly) linked lists, determine if the two lists intersect. Return
the intersecting node. Note that the intersection is defined based on reference, not value. That is,
if the k-th node of the first linked list is the exact same node (by reference) as the j-th node of
the second linked list, then they are intersecting.

"""
import unittest
from .linked_list import LinkedList


def get_intersection(lst1, lst2):
    """
    Find intersection node for two linked lists.

    Complexity: O(N + M) time, O(1) space.

    Args:
        lst1 (LinkedList): First linked list
        lst2 (LinkedList): Second linked list

    Returns:
        ListNode: Common intersection node or None

    """
    if lst1.head is None or lst2.head is None:
        return None

    len1 = 1
    tail1 = lst1.head
    while tail1.next:
        len1 += 1
        tail1 = tail1.next

    len2 = 1
    tail2 = lst2.head
    while tail2.next:
        len2 += 1
        tail2 = tail2.next

    if tail1 is not tail2:
        return None

    runner1 = lst1.head
    runner2 = lst2.head
    if len2 > len1:
        for i in range(len2 - len1):
            runner2 = runner2.next
    elif len1 > len2:
        for i in range(len1 - len2):
            runner1 = runner1.next

    while runner1 is not runner2:
        runner1 = runner1.next
        runner2 = runner2.next

    return runner1


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
        ([0], [], [1, 2, 3, 4]),
        ([0, 1], [], [2, 3, 4]),
        ([0, 1], [1], [2, 3, 4]),
        ([0, 1, 2], [2], [3, 4]),
        ([0, 1, 2, 3], [], [4]),
        ([0, 1, 2, 3], [1, 2, 3], [4]),
        ([0, 1, 2, 3, 4], [4], []),
        ([0, 1, 2, 3, 4], [1, 2, 3, 4], []),
        ([0], [0], [1, 2, 3, 4, 5]),
        ([0, 1, 2], [1, 2], [3, 4, 5]),
        ([0, 1, 2, 3], [0, 1, 2, 3], [4, 5]),
        ([0, 1, 2, 3, 4], [4], [5]),
        ([0, 1, 2, 3, 4], [2, 3, 4], [5]),
        ([0, 1, 2, 3, 4, 5], [], []),
        ([0, 1, 2, 3, 4, 5], [4, 5], []),
        ([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], []),
        ([], [], [0, 1, 2, 3, 4, 5, 6]),
        ([0, 1], [0, 1], [2, 3, 4, 5, 6]),
        ([0, 1, 2], [0, 1, 2], [3, 4, 5, 6]),
        ([0, 1, 2, 3], [1, 2, 3], [4, 5, 6]),
        ([0, 1, 2, 3, 4], [], [5, 6]),
        ([0, 1, 2, 3, 4], [4], [5, 6]),
        ([0, 1, 2, 3, 4], [1, 2, 3, 4], [5, 6]),
        ([0, 1, 2, 3, 4, 5], [4, 5], [6]),
        ([0, 1, 2, 3, 4, 5], [2, 3, 4, 5], [6]),
        ([0, 1, 2, 3, 4, 5], [0, 1, 2, 3, 4, 5], [6]),
        ([0, 1, 2, 3, 4, 5, 6], [4, 5, 6], []),
        ([0, 1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6], [])
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
