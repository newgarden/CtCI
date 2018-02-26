# -*- coding: utf-8 -*-
"""
Delete Middle Node

Problem statement: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only
access to that node.

Example:
    Input: The node c from the linked list a -> b -> c -> d -> e -> f
    Result: Nothing is returned, but the new linked list looks like a -> b -> d -> e -> f

"""
import unittest
from linked_list import LinkedList


def delete_middle_node(node):
    """
    Deletes a node from a list. If it is the last node do nothing.

    Complexity: O(1) time, O(1) space.

    Args:
        node (ListNode): Node to delete.

    """
    if not node.next:
        return
    node.value = node.next.value
    node.next = node.next.next


class TestDeleteMiddleNode(unittest.TestCase):

    def test_delete_middle_node(self):
        lst = LinkedList(['a', 'b', 'c', 'd', 'e', 'f', 'g'])

        delete_middle_node(lst[6])
        self.assertEqual(lst, LinkedList(['a', 'b', 'c', 'd', 'e', 'f', 'g']))

        delete_middle_node(lst[5])
        self.assertEqual(lst, LinkedList(['a', 'b', 'c', 'd', 'e', 'g']))

        delete_middle_node(lst[2])
        self.assertEqual(lst, LinkedList(['a', 'b', 'd', 'e', 'g']))

        delete_middle_node(lst[0])
        self.assertEqual(lst, LinkedList(['b', 'd', 'e', 'g']))

        delete_middle_node(lst[1])
        self.assertEqual(lst, LinkedList(['b', 'e', 'g']))

        delete_middle_node(lst[1])
        self.assertEqual(lst, LinkedList(['b', 'g']))

        delete_middle_node(lst[0])
        self.assertEqual(lst, LinkedList(['g']))


if __name__ == '__main__':
    unittest.main()
