# -*- coding: utf-8 -*-
import unittest


class ListNode:
    """
    Node of a linked list.
    """

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class DListNode:
    """
    Node of a doubly linked list.
    """

    def __init__(self, value, prev_node=None, next_node=None, ):
        self.value = value
        self.prev = prev_node
        self.next = next_node


class TestListNode(unittest.TestCase):
    """
    Test for ListNode class.
    """

    def test_init(self):
        """
        Test __init__() method.
        """
        node1 = ListNode(1)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.next, None)

        node2 = ListNode(value=2, next_node=node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.next, node1)


class TestDListNode(unittest.TestCase):
    """
    Test for DListNode class.
    """

    def test_init(self):
        """
        Test __init__() method.
        """
        node1 = DListNode(1)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.next, None)
        self.assertEqual(node1.prev, None)

        node2 = DListNode(2, node1, None)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.prev, node1)
        self.assertEqual(node2.next, None)

        node3 = DListNode(value=3, next_node=node1)
        self.assertEqual(node3.value, 3)
        self.assertEqual(node3.prev, None)
        self.assertEqual(node3.next, node1)


if __name__ == '__main__':
    unittest.main()
