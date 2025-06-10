"""
Return Kth to Last.

Problem statement: Implement an algorithm to find the k-th to last element of a singly linked list.

"""
import unittest

from .linked_list import LinkedList


def get_kth_to_last(lst, k):
    """
    Find k-th to last node of a singly linked list.

    Complexity: O(N) time, O(1) space.

    Args:
        lst (LinkedList): A singly linked list.
        k (int): Node index starting from the end.

    Returns:
        ListNode: K-th to last node or None if k is out of bounds. Indexing is 1-based, which
            means that k = 1 will return the last element.

    """
    runner = lst.head
    for i in range(k):
        if not runner:
            return None
        runner = runner.next

    result = lst.head
    while runner:
        runner = runner.next
        result = result.next

    return result


class TestKthToLast(unittest.TestCase):

    def test_get_kth_to_last(self):
        lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(get_kth_to_last(lst, 1).value, 10)
        self.assertEqual(get_kth_to_last(lst, 2).value, 9)
        self.assertEqual(get_kth_to_last(lst, 3).value, 8)
        self.assertEqual(get_kth_to_last(lst, 5).value, 6)
        self.assertEqual(get_kth_to_last(lst, 10).value, 1)
        self.assertEqual(get_kth_to_last(lst, 11), None)
        self.assertEqual(get_kth_to_last(lst, 12), None)
        self.assertEqual(get_kth_to_last(lst, 15), None)
        self.assertEqual(get_kth_to_last(lst, 0), None)
        self.assertEqual(get_kth_to_last(lst, -1), None)

        lst = LinkedList()
        self.assertEqual(get_kth_to_last(lst, 0), None)
        self.assertEqual(get_kth_to_last(lst, 1), None)
        self.assertEqual(get_kth_to_last(lst, 2), None)

        lst = LinkedList(['a'])
        self.assertEqual(get_kth_to_last(lst, 0), None)
        self.assertEqual(get_kth_to_last(lst, 1).value, 'a')
        self.assertEqual(get_kth_to_last(lst, 2), None)

        lst = LinkedList(['a', 'b'])
        self.assertEqual(get_kth_to_last(lst, 0), None)
        self.assertEqual(get_kth_to_last(lst, 1).value, 'b')
        self.assertEqual(get_kth_to_last(lst, 2).value, 'a')
        self.assertEqual(get_kth_to_last(lst, 3), None)
