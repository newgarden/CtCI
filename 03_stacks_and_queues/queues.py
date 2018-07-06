# -*- coding: utf-8 -*-
import unittest


class QueueError(Exception):
    """
    Base queue exception.
    """
    pass


class EmptyQueueError(QueueError):
    """
    Raised if peek() or pop() is attempted on an empty queue.
    """
    pass


class QueueItem:
    """
    """
    __slots__ = ('value', 'next')

    def __init__(self, value, next_item=None):
        self.value = value
        self.next = next_item


class Queue:

    def __init__(self):
        self._front = None
        self._rear = None

    def add(self, value):
        if not self._front:
            self._rear = self._front = QueueItem(value)
        else:
            new_item = QueueItem(value)
            self._rear.next = new_item
            self._rear = new_item

    def remove(self):
        if not self._front:
            raise EmptyQueueError
        value = self._front.value
        self._front = self._front.next
        if not self._front:
            self._rear = None
        return value

    def peek(self):
        if not self._front:
            raise EmptyQueueError
        return self._front.value

    def is_empty(self):
        return self._front is None


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def _check_state(self, front=None):
        if front is None:
            self.assertIs(self.queue.is_empty(), True)
            self.assertRaises(EmptyQueueError, self.queue.peek)
            self.assertRaises(EmptyQueueError, self.queue.remove)
        else:
            self.assertIs(self.queue.is_empty(), False)
            self.assertEqual(self.queue.peek(), front)

    def test_queue(self):
        q = self.queue
        self._check_state(None)           # ()

        q.add(1)
        self._check_state(1)              # (1)

        self.assertEqual(q.remove(), 1)
        self._check_state(None)           # ()

        q.add(2)
        self._check_state(2)              # (2)

        q.add(3)
        self._check_state(2)              # (2, 3)

        self.assertEqual(q.remove(), 2)
        self._check_state(3)              # (3)

        self.assertEqual(q.remove(), 3)
        self._check_state(None)           # ()

        q.add(4)
        self._check_state(4)              # (4)

        q.add(5)
        self._check_state(4)              # (4, 5)

        q.add(6)
        self._check_state(4)              # (4, 5, 6)

        self.assertEqual(q.remove(), 4)
        self._check_state(5)              # (5, 6)

        self.assertEqual(q.remove(), 5)
        self._check_state(6)              # (6)

        self.assertEqual(q.remove(), 6)
        self._check_state(None)           # ()

        q.add(7)
        self._check_state(7)              # (7)

        q.add(8)
        self._check_state(7)              # (7, 8)

        self.assertEqual(q.remove(), 7)
        self._check_state(8)              # (8)

        q.add(9)
        self._check_state(8)              # (8, 9)

        q.add(10)
        self._check_state(8)              # (8, 9, 10)

        self.assertEqual(q.remove(), 8)
        self._check_state(9)              # (9, 10)

        q.add(11)
        self._check_state(9)              # (9, 10, 11)

        q.add(12)
        self._check_state(9)              # (9, 10, 11, 12)

        self.assertEqual(q.remove(), 9)
        self._check_state(10)             # (10, 11, 12)

        q.add(13)
        self._check_state(10)             # (10, 11, 12, 13)

        q.add(14)
        self._check_state(10)             # (10, 11, 12, 13, 14)

        self.assertEqual(q.remove(), 10)
        self._check_state(11)             # (11, 12, 13, 14)

        self.assertEqual(q.remove(), 11)
        self._check_state(12)             # (12, 13, 14)

        q.add(15)
        self._check_state(12)             # (12, 13, 14, 15)

        self.assertEqual(q.remove(), 12)
        self._check_state(13)             # (13, 14, 15)

        self.assertEqual(q.remove(), 13)
        self._check_state(14)             # (14, 15)

        q.add(16)
        self._check_state(14)             # (14, 15, 16)

        self.assertEqual(q.remove(), 14)
        self._check_state(15)             # (15, 16)

        self.assertEqual(q.remove(), 15)
        self._check_state(16)             # (16)

        q.add(17)
        self._check_state(16)             # (16, 17)

        self.assertEqual(q.remove(), 16)
        self._check_state(17)             # (17)

        self.assertEqual(q.remove(), 17)
        self._check_state(None)           # ()
