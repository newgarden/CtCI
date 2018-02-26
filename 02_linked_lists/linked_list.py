# -*- coding: utf-8 -*-
"""
Implementation of linked list and doubly linked list data structures.

This implementation is simplified to provide the minimum functionality needed for solving the
problems from chapter 2.

Provides four classes:

    1) LinkedList - singly linked list.
    2) DLinkedList - doubly linked list.
    3) ListNode - node of a LinkedList.
    4) DListNode - node of a DLinkedList.

Both LinkedList and DLinkedList can handle circular lists. In a circular linked list the last node
has a link to the head of the list. A list may change form being circular and non-circular during
runtime depending on the last node's next_node pointer.

"""
import unittest


class ListNode:
    """
    Node of a linked list.

    Attributes:
        value: Value of the node. It can be any object.
        next_node (ListNode): Link to the next node in the list or None.

    """

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class DListNode:
    """
    Node of a doubly linked list.

    Attributes:
        value: Value of the node. It can be any object.
        prev_node (DListNode): Link to the previous node in the list or None.
        next_node (DListNode): Link to the next node in the list or None.

    """

    def __init__(self, value, prev_node=None, next_node=None):
        self.value = value
        self.prev = prev_node
        self.next = next_node


class LinkedList:
    """
    Singly linked list.

    Attributes:
        head (ListNode): First node of the list. None for empty list.

    """

    def __init__(self, iterable=None, circular=False):
        """
        Initialize linked list using values from an iterable.

        Args:
            iterable: Optional iterable of arbitrary objects used to populate the list.
            circular (bool): It True then the last node of the list will have a link to the head,
                making the list circular. This flag has affect only when the list is populated from
                an iterable.

        """
        self.head = None
        if iterable:
            value_iter = iter(iterable)
            node = None
            try:
                self.head = ListNode(next(value_iter))
                node = self.head
                while True:
                    node.next = ListNode(next(value_iter))
                    node = node.next
            except StopIteration:
                if node and circular:
                    node.next = self.head

    def __repr__(self):
        if not self.head:
            return 'LinkedList()'
        node = self.head
        repr_nodes = []
        while node:
            repr_nodes.append(repr(node.value))
            node = node.next
            if node is self.head:
                return 'LinkedList([{}], circular=True)'.format(', '.join(repr_nodes))
        return 'LinkedList([{}])'.format(', '.join(repr_nodes))

    def __str__(self):
        if not self.head:
            return '<LinkedList>'
        node = self.head
        repr_nodes = []
        while node:
            repr_nodes.append(repr(node.value))
            node = node.next
            if node is self.head:
                return '<Circular LinkedList: {}>'.format(', '.join(repr_nodes))
        return '<LinkedList: {}>'.format(', '.join(repr_nodes))

    def __eq__(self, other):
        """
        Test two lists for equality.

        Two lists are considered equal if they have the same length and values of their
        corresponding nodes are equal.

        """
        node1 = self.head
        node2 = other.head
        while node1 and node2:
            if node1.value != node2.value:
                return False
            node1 = node1.next
            node2 = node2.next
            if node1 is self.head or node2 is other.head:
                break
        if (node1 is None) and (node2 is None):
            return True
        if (node1 is not None) and (node2 is not None):
            if (node1 is self.head) and (node2 is other.head):
                return True
        return False

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError('linked list indices must be integers')

        if not self.head or key < 0:
            raise IndexError('linked list index out of range')

        i = 0
        node = self.head
        while i < key:
            if not node.next or node.next is self.head:
                raise IndexError('linked list index out of range')
            node = node.next
            i += 1

        return node


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


class TestLinkedList(unittest.TestCase):
    """
    Test for LinkedList class.
    """

    def test_init(self):
        """
        Test __init__() method.
        """

        # Test edge case when iterable is empty
        lst = LinkedList()
        self.assertEqual(lst.head, None)
        lst = LinkedList([])
        self.assertEqual(lst.head, None)
        lst = LinkedList('')
        self.assertEqual(lst.head, None)
        lst = LinkedList([], circular=True)
        self.assertEqual(lst.head, None)

        # Test on different kind of iterables
        iterables = [
            'qwertyuiop',
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
            (1, 'a', 'abc', [1, 2, 3], ('a', 'b', 1), None)
        ]
        for iterable in iterables:
            lst = LinkedList(iterable)
            self.assertEqual(lst.head.value, iterable[0])
            node = lst.head
            for value in iterable:
                self.assertEqual(node.value, value)
                node = node.next
            self.assertEqual(node, None)

        # Test on iterators
        for iterable in iterables:
            lst = LinkedList(iter(iterable))
            self.assertEqual(lst.head.value, iterable[0])
            node = lst.head
            for value in iterable:
                self.assertEqual(node.value, value)
                node = node.next
            self.assertEqual(node, None)

        # Test creation of a circular list
        lst = LinkedList(['a', 'b', 'c'], circular=True)
        self.assertIs(lst.head.next.next.next, lst.head)

        lst = LinkedList([1], circular=True)
        self.assertIs(lst.head.next, lst.head)

    def test_str(self):
        """
        Test __str__() method.
        """
        lst = LinkedList()
        self.assertEqual(str(lst), '<LinkedList>')

        lst = LinkedList([1, 'a', True, (2, 'b'), [1, 2, 3]])
        self.assertEqual(str(lst), "<LinkedList: 1, 'a', True, (2, 'b'), [1, 2, 3]>")

        lst = LinkedList([1, 2, 3], circular=True)
        self.assertEqual(str(lst), '<Circular LinkedList: 1, 2, 3>')

    def test_repr(self):
        """
        Test __repr__() method.
        """
        lst = LinkedList()
        self.assertEqual(repr(lst), 'LinkedList()')

        lst = LinkedList([1, 'a', True, (2, 'b'), [1, 2, 3]])
        self.assertEqual(repr(lst), "LinkedList([1, 'a', True, (2, 'b'), [1, 2, 3]])")

        lst = LinkedList([1, 2, 3], circular=True)
        self.assertEqual(repr(lst), 'LinkedList([1, 2, 3], circular=True)')

    def test_eq(self):
        """
        Test __eq__() method.
        """
        empty_lst1 = LinkedList()
        empty_lst2 = LinkedList()
        lst1 = LinkedList([1, 2, 3])
        lst2 = LinkedList((1, 2, 3))
        lst3 = LinkedList([1, 2])
        lst4 = LinkedList([1, 0, 3])
        lst5 = LinkedList([0, 2, 3])
        circular_empty_lst1 = LinkedList(circular=True)
        circular_empty_lst2 = LinkedList(circular=True)
        circular_lst1 = LinkedList([1, 2, 3], circular=True)
        circular_lst2 = LinkedList((1, 2, 3), circular=True)
        circular_lst3 = LinkedList([1, 2], circular=True)
        circular_lst4 = LinkedList([1, 0, 3], circular=True)
        circular_lst5 = LinkedList([0, 2, 3], circular=True)

        self.assertEqual(empty_lst1, empty_lst1)
        self.assertEqual(empty_lst1, empty_lst2)
        self.assertNotEqual(empty_lst1, lst1)
        self.assertEqual(empty_lst1, circular_empty_lst1)
        self.assertNotEqual(empty_lst1, circular_lst1)

        self.assertNotEqual(lst1, empty_lst1)
        self.assertEqual(lst1, lst1)
        self.assertEqual(lst1, lst2)
        self.assertNotEqual(lst1, lst3)
        self.assertNotEqual(lst1, lst4)
        self.assertNotEqual(lst1, lst5)
        self.assertNotEqual(lst1, circular_empty_lst1)
        self.assertNotEqual(lst1, circular_lst1)
        self.assertNotEqual(lst1, circular_lst3)
        self.assertNotEqual(lst1, circular_lst4)

        self.assertNotEqual(lst3, lst1)
        self.assertNotEqual(lst3, lst4)
        self.assertNotEqual(lst3, lst5)
        self.assertNotEqual(lst3, circular_lst1)
        self.assertNotEqual(lst3, circular_lst4)
        self.assertNotEqual(lst3, circular_lst5)

        self.assertEqual(circular_empty_lst1, empty_lst1)
        self.assertNotEqual(circular_empty_lst1, lst1)
        self.assertEqual(circular_empty_lst1, circular_empty_lst1)
        self.assertEqual(circular_empty_lst1, circular_empty_lst2)
        self.assertNotEqual(circular_empty_lst1, circular_lst1)

        self.assertNotEqual(circular_lst1, empty_lst1)
        self.assertNotEqual(circular_lst1, lst1)
        self.assertNotEqual(circular_lst1, lst3)
        self.assertNotEqual(circular_lst1, lst4)
        self.assertNotEqual(circular_lst1, lst5)
        self.assertNotEqual(circular_lst1, circular_empty_lst1)
        self.assertEqual(circular_lst1, circular_lst1)
        self.assertEqual(circular_lst1, circular_lst2)
        self.assertNotEqual(circular_lst1, circular_lst3)
        self.assertNotEqual(circular_lst1, circular_lst3)
        self.assertNotEqual(circular_lst1, circular_lst4)

    def test_getitem(self):
        lst = LinkedList()

        with self.assertRaises(TypeError) as cm:
            node = lst['1']
        self.assertEqual(str(cm.exception), 'linked list indices must be integers')

        with self.assertRaises(TypeError) as cm:
            node = lst[2:5]

        with self.assertRaises(IndexError) as cm:
            node = lst[0]
        self.assertEqual(str(cm.exception), 'linked list index out of range')

        lst = LinkedList(['a', 'b', 'c', 'd', 'e'])

        with self.assertRaises(IndexError) as cm:
            node = lst[-1]

        with self.assertRaises(IndexError) as cm:
            node = lst[5]

        self.assertEqual(lst[0].value, 'a')
        self.assertEqual(lst[2].value, 'c')
        self.assertEqual(lst[4].value, 'e')

        lst = LinkedList(['1', '2', '3', '4', '5'], circular=True)

        with self.assertRaises(IndexError) as cm:
            node = lst[-1]

        with self.assertRaises(IndexError) as cm:
            node = lst[5]

        self.assertEqual(lst[0].value, '1')
        self.assertEqual(lst[2].value, '3')
        self.assertEqual(lst[4].value, '5')


if __name__ == '__main__':
    unittest.main()
