# -*- coding: utf-8 -*-
"""
Queue via Stacks:

Implement a MyQueue class which implements a queue using two stacks.

"""
import unittest

from .stack import Stack, EmptyQueueError


class MyQueue:
    """
    Queue implementation using two stacks.

    One of the stacks serves as the tail of the queue, we push elements to it. Second one is the
    head, we pop/peek elements from it.

               head       tail
            * - - - - * - - - - *
    pop <-- |         |         | <-- push
            * - - - - * - - - - -
          top       bottom      top

    Algorithm for pushing elements to the queue is trivial, just push it to the tail. Pop and peek
    operations are bit more complex:

        1. If head and tail are empty, raise exception.
        2. If head is not empty, pop/peek the element and return.
        3. If head is empty, transfer all the elements from the tail to the head. During the
           transfer elements order reversed so that the newest elements will in the bottom of the
           head, while oldest will in the top.
        4. Pop/peek the element from the head. Return.

    Transfer between stacks takes O(N) time, but since each element must be transferred only once
    the amortized cost of pop and peek is O(1).

    """

    def __init__(self):
        self._tail = Stack()
        self._head = Stack()

    def add(self, value):
        self._tail.push(value)

    def remove(self):
        if self._head.is_empty():
            if self._tail.is_empty():
                raise EmptyQueueError
            while not self._tail.is_empty():
                self._head.push(self._tail.pop())
        return self._head.pop()

    def peek(self):
        if self._head.is_empty():
            if self._tail.is_empty():
                raise EmptyQueueError
            while not self._tail.is_empty():
                self._head.push(self._tail.pop())
        return self._head.peek()

    def is_empty(self):
        return self._head.is_empty() and self._tail.is_empty()


class TestMyQueue(unittest.TestCase):

    def _check_state(self, queue, expected_state):
        if expected_state == ():
            self.assertIs(queue.is_empty(), True)
            self.assertRaises(EmptyQueueError, queue.peek)
            self.assertRaises(EmptyQueueError, queue.remove)
        else:
            self.assertIs(queue.is_empty(), False)
            self.assertEqual(queue.peek(), expected_state[0])

    def test_my_queue(self):
        q = MyQueue()                                   # head tail
        self._check_state(q, ())                        # () ()

        q.add(1)
        self._check_state(q, (1,))                      # () (1)

        self.assertEqual(q.remove(), 1)
        self._check_state(q, ())                        # () ()

        q.add(2)
        self._check_state(q, (2,))                      # () (2)

        q.add(3)
        self._check_state(q, (2, 3))                    # () (2, 3)

        self.assertEqual(q.remove(), 2)
        self._check_state(q, (3,))                      # (3) ()

        self.assertEqual(q.remove(), 3)
        self._check_state(q, ())                        # () ()

        q.add(4)
        self._check_state(q, (4,))                      # () (4)

        q.add(5)
        self._check_state(q, (4, 5))                    # () (4, 5)

        q.add(6)
        self._check_state(q, (4, 5, 6))                 # () (4, 5, 6)

        self.assertEqual(q.remove(), 4)
        self._check_state(q, (5, 6))                    # (5, 6) ()

        q.add(7)
        self._check_state(q, (5, 6, 7))                 # (5, 6) (7)

        self.assertEqual(q.remove(), 5)
        self._check_state(q, (6, 7))                    # (6) (7)

        q.add(8)
        self._check_state(q, (6, 7, 8))                 # (6) (7, 8)

        self.assertEqual(q.remove(), 6)
        self._check_state(q, (7, 8))                    # () (7, 8)

        q.add(9)
        self._check_state(q, (7, 8, 9))                 # () (7, 8, 9)

        self.assertEqual(q.remove(), 7)
        self._check_state(q, (8, 9))                    # (8, 9) ()

        q.add(10)
        self._check_state(q, (8, 9, 10))                # (8, 9) (10)

        q.add(11)
        self._check_state(q, (8, 9, 10, 11))            # (8, 9) (10, 11)

        q.add(12)
        self._check_state(q, (8, 9, 10, 11, 12))        # (8, 9) (10, 11, 12)

        self.assertEqual(q.remove(), 8)
        self._check_state(q, (9, 10, 11, 12))           # (9) (10, 11, 12)

        self.assertEqual(q.remove(), 9)
        self._check_state(q, (10, 11, 12))              # () (10, 11, 12)

        self.assertEqual(q.remove(), 10)
        self._check_state(q, (11, 12))                  # (11, 12) ()

        q.add(13)
        self._check_state(q, (11, 12, 13))              # (11, 12) (13)

        q.add(14)
        self._check_state(q, (11, 12, 13, 14))          # (11, 12) (13, 14)

        q.add(15)
        self._check_state(q, (11, 12, 13, 14, 15))      # (11, 12) (13, 14, 15)

        q.add(16)
        self._check_state(q, (11, 12, 13, 14, 15, 16))  # (11, 12) (13, 14, 15, 16)

        self.assertEqual(q.remove(), 11)
        self._check_state(q, (12, 13, 14, 15, 16))      # (12) (13, 14, 15, 16)

        self.assertEqual(q.remove(), 12)
        self._check_state(q, (13, 14, 15, 16))          # () (13, 14, 15, 16)

        q.add(17)
        self._check_state(q, (13, 14, 15, 16, 17))      # () (13, 14, 15, 16, 17)

        self.assertEqual(q.remove(), 13)
        self._check_state(q, (14, 15, 16, 17))          # (14, 15, 16, 17) ()

        self.assertEqual(q.remove(), 14)
        self._check_state(q, (15, 16, 17))              # (15, 16, 17) ()

        q.add(18)
        self._check_state(q, (15, 16, 17, 18))          # (15, 16, 17) (18)

        self.assertEqual(q.remove(), 15)
        self._check_state(q, (16, 17, 18))              # (16, 17) (18)

        self.assertEqual(q.remove(), 16)
        self._check_state(q, (17, 18))                  # (17) (18)

        q.add(19)
        self._check_state(q, (17, 18, 19))              # (17) (18, 19)

        self.assertEqual(q.remove(), 17)
        self._check_state(q, (18, 19))                  # () (18, 19)

        self.assertEqual(q.remove(), 18)
        self._check_state(q, (19,))                     # (19) ()

        q.add(20)
        self._check_state(q, (19, 20))                  # (19) (20)

        self.assertEqual(q.remove(), 19)
        self._check_state(q, (20,))                     # () (20)

        self.assertEqual(q.remove(), 20)
        self._check_state(q, ())                        # () ()
