"""
Simple implementation of linked list data structure for use in exercises from chapter 2.
"""
import unittest


class ListNode:
    """
    Node of a linked list.

    Args:
        value: Value of the node. It can be any object.
        next_node (ListNode): Pointer to the next node in the list or None.

    Attributes:
        value: Value of the node. It can be any object.
        next (ListNode): Pointer to the next node in the list or None.

    """
    __slots__ = ('value', 'next')

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    """
    Singly linked list.

    Args:
        iterable: Optional iterable of arbitrary objects used to populate the list.

    Attributes:
        head (ListNode): First node of the list. None for empty list.

    """

    def __init__(self, iterable=None):
        self.head = None
        if iterable:
            value_iter = iter(iterable)
            try:
                self.head = ListNode(next(value_iter))
                node = self.head
                while True:
                    node.next = ListNode(next(value_iter))
                    node = node.next
            except StopIteration:
                pass

    def __repr__(self):
        if not self.head:
            return 'LinkedList()'
        node = self.head
        repr_nodes = []
        while node:
            repr_nodes.append(repr(node.value))
            node = node.next
        return 'LinkedList([{}])'.format(', '.join(repr_nodes))

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
        if (node1 is None) and (node2 is None):
            return True
        return False

    def __getitem__(self, key):
        """
        Get node by index.

        Returns:
            ListNode

        Raises:
            TypeError: If key is not an integer.
            IndexError: If index is out of range or negative.

        """
        if not isinstance(key, int):
            raise TypeError('linked list indices must be integers')

        if not self.head or key < 0:
            raise IndexError('linked list index out of range')

        i = 0
        node = self.head
        while i < key:
            if not node.next:
                raise IndexError('linked list index out of range')
            node = node.next
            i += 1

        return node


class TestListNode(unittest.TestCase):
    """
    Test for ListNode class.
    """

    def test_init(self):
        node1 = ListNode(1)
        self.assertEqual(node1.value, 1)
        self.assertEqual(node1.next, None)

        node2 = ListNode(value=2, next_node=node1)
        self.assertEqual(node2.value, 2)
        self.assertEqual(node2.next, node1)


class TestLinkedList(unittest.TestCase):
    """
    Test for LinkedList class.
    """

    def test_init(self):
        # Test edge case when iterable is empty
        lst = LinkedList()
        self.assertEqual(lst.head, None)
        lst = LinkedList([])
        self.assertEqual(lst.head, None)
        lst = LinkedList('')
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

    def test_repr(self):
        lst = LinkedList()
        self.assertEqual(repr(lst), 'LinkedList()')

        lst = LinkedList([1, 'a', True, (2, 'b'), [1, 2, 3]])
        self.assertEqual(repr(lst), "LinkedList([1, 'a', True, (2, 'b'), [1, 2, 3]])")

    def test_eq(self):
        empty_lst1 = LinkedList()
        empty_lst2 = LinkedList()
        lst1 = LinkedList([1, 2, 3])
        lst2 = LinkedList((1, 2, 3))
        lst3 = LinkedList([1, 2])
        lst4 = LinkedList([1, 0, 3])
        lst5 = LinkedList([0, 2, 3])

        self.assertEqual(empty_lst1, empty_lst1)
        self.assertEqual(empty_lst1, empty_lst2)

        self.assertNotEqual(empty_lst1, lst1)
        self.assertNotEqual(lst1, empty_lst1)

        self.assertEqual(lst1, lst1)
        self.assertEqual(lst1, lst2)

        self.assertNotEqual(lst1, lst3)
        self.assertNotEqual(lst1, lst4)
        self.assertNotEqual(lst1, lst5)
        self.assertNotEqual(lst3, lst1)
        self.assertNotEqual(lst3, lst4)
        self.assertNotEqual(lst3, lst5)

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
