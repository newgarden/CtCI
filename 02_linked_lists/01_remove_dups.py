# -*- coding: utf-8 -*-
"""
Remove dups.

Problem statement: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP: How would you solve this problem if a temporary buffer is not allowed?

"""
import unittest

from linked_list import LinkedList


def remove_dups1(lst):
    """
    Remove duplicates from a linked list using a temporary buffer.

    Takes O(N) time and O(N) additional space.

    Args:
        lst (LinkedList): Linked list containing any hashable objects.

    """
    node = lst.head
    if not node:
        return

    values = set()
    values.add(node.value)

    while node.next:
        if node.next.value in values:
            node.next = node.next.next
        else:
            node = node.next
            values.add(node.value)


def remove_dups2(lst):
    """
    Remove duplicates from a linked list without using additional memory.

    Takes O(N^2) time and O(1) additional space.

    Args:
        lst (LinkedList): Linked list containing arbitrary objects.

    """
    current = lst.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next


class TestRemoveDups(unittest.TestCase):
    data = [
        ([], []),
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([1, 1], [1]),
        (['a', 'a', 'a'], ['a']),
        (['a', 'b', 'a', 'b'], ['a', 'b']),
        ([1, 2, 3, 2, 4, 3, 3, 5, 5, 5], [1, 2, 3, 4, 5]),
        ([1, 1, 2, 1, 2, 2, 3], [1, 2, 3]),
        ('aaabbcccbbaaa', 'abc'),
        ([None, 1, 'ab', 1, (1, 2), '1', 'ab', (1, 2), None], [None, 1, 'ab', (1, 2), '1']),
    ]

    def test_remove_dups1(self):
        for data in self.data:
            lst = LinkedList(data[0])
            remove_dups1(lst)
            self.assertEqual(lst, LinkedList(data[1]))

    def test_remove_dups2(self):
        for data in self.data:
            lst = LinkedList(data[0])
            remove_dups2(lst)
            self.assertEqual(lst, LinkedList(data[1]))


if __name__ == '__main__':
    unittest.main()
