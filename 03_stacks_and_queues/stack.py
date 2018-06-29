# -*- coding: utf-8 -*-
import unittest


class StackError(Exception):
    """
    Base stack exception.
    """
    pass


class QueueError(Exception):
    """
    Base queue exception
    """
    pass


class EmptyStackError(StackError):
    """
    Raised if peek() or pop() is attempted on an empty stack.
    """
    pass


class StackOverflowError(StackError):
    """
    Raised if a new element cannot be pushed to a stack because it has reached its full capacity.
    """
    pass


class EmptyQueueError(QueueError):
    """
    Raised if peek() or pop() is attempted on an empty queue.
    """
    pass


class StackItem:
    """
    """
    __slots__ = ('value', 'next')

    def __init__(self, value, next_item=None):
        self.value = value
        self.next = next_item


class Stack:

    def __init__(self):
        self._top = None

    def push(self, value):
        self._top = StackItem(value, self._top)

    def pop(self):
        if not self._top:
            raise EmptyStackError
        value = self._top.value
        self._top = self._top.next
        return value

    def peek(self):
        if self._top is None:
            raise EmptyStackError
        return self._top.value

    def is_empty(self):
        return self._top is None


class LimitedStack(Stack):

    def __init__(self, capacity):
        super(LimitedStack, self).__init__()
        self._capacity = capacity
        self._length = 0

    def __len__(self):
        return self._length

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if self._length > value:
            raise StackOverflowError
        self._capacity = value

    def push(self, value):
        if self._length >= self._capacity:
            raise StackOverflowError
        super(LimitedStack, self).push(value)
        self._length += 1

    def pop(self):
        value = super(LimitedStack, self).pop()
        self._length -= 1
        return value

    def is_full(self):
        return self._length == self._capacity


class TestStack(unittest.TestCase):

    def _check_stack_state(self, s, is_empty, top=None):
        self.assertIs(s.is_empty(), is_empty)
        if is_empty:
            self.assertRaises(EmptyStackError, s.pop)
            self.assertRaises(EmptyStackError, s.peek)
        else:
            self.assertEqual(s.peek(), top)

    def test_stack(self):
        # []
        s = Stack()
        self._check_stack_state(s, is_empty=True)

        # [1]
        s.push(1)
        self._check_stack_state(s, is_empty=False, top=1)

        # []
        self.assertEqual(s.pop(), 1)
        self._check_stack_state(s, is_empty=True)

        # [2]
        s.push(2)
        self._check_stack_state(s, is_empty=False, top=2)

        # [2 3]
        s.push(3)
        self._check_stack_state(s, is_empty=False, top=3)

        # [2]
        self.assertEqual(s.pop(), 3)
        self._check_stack_state(s, is_empty=False, top=2)

        # [2 4]
        s.push(4)
        self._check_stack_state(s, is_empty=False, top=4)

        # [2 4 5]
        s.push(5)
        self._check_stack_state(s, is_empty=False, top=5)

        # [2 4]
        self.assertEqual(s.pop(), 5)
        self._check_stack_state(s, is_empty=False, top=4)

        # [2]
        self.assertEqual(s.pop(), 4)
        self._check_stack_state(s, is_empty=False, top=2)

        # []
        self.assertEqual(s.pop(), 2)
        self._check_stack_state(s, is_empty=True)


class TestLimitedStack(unittest.TestCase):

    def _check_stack_state(self, s, is_empty, is_full, length, capacity, top=None):
        self.assertIs(s.is_empty(), is_empty)
        if is_empty:
            self.assertRaises(EmptyStackError, s.pop)
            self.assertRaises(EmptyStackError, s.peek)
        else:
            self.assertEqual(s.peek(), top)

        self.assertIs(s.is_full(), is_full)
        if is_full:
            self.assertRaises(StackOverflowError, s.push, 100)

        self.assertEqual(len(s), length)
        self.assertEqual(s.capacity, capacity)

    def test_limited_stack(self):
        # (_ _ _ _)
        s = LimitedStack(4)
        self._check_stack_state(s, is_empty=True, is_full=False, length=0, capacity=4)

        # (1 _ _ _)
        s.push(1)
        self._check_stack_state(s, is_empty=False, is_full=False, length=1, capacity=4, top=1)

        # (1 2 _ _)
        s.push(2)
        self._check_stack_state(s, is_empty=False, is_full=False, length=2, capacity=4, top=2)

        # (1 2 3 _)
        s.push(3)
        self._check_stack_state(s, is_empty=False, is_full=False, length=3, capacity=4, top=3)

        # (1 2 3 4)
        s.push(4)
        self._check_stack_state(s, is_empty=False, is_full=True, length=4, capacity=4, top=4)

        # (1 2 3 4 _ _)
        s.capacity = 6
        self._check_stack_state(s, is_empty=False, is_full=False, length=4, capacity=6, top=4)

        # (1 2 3 4 5 _)
        s.push(5)
        self._check_stack_state(s, is_empty=False, is_full=False, length=5, capacity=6, top=5)
        self.assertRaises(StackOverflowError, setattr, s, 'capacity', 4)

        s.push(6)  # (1 2 3 4 5 6)
        self._check_stack_state(s, is_empty=False, is_full=True, length=6, capacity=6, top=6)

        # (1 2 3 4 5 _)
        self.assertEqual(s.pop(), 6)
        self._check_stack_state(s, is_empty=False, is_full=False, length=5, capacity=6, top=5)

        # (1 2 3 4 _ _)
        self.assertEqual(s.pop(), 5)
        self._check_stack_state(s, is_empty=False, is_full=False, length=4, capacity=6, top=4)

        # (1 2 3 4)
        s.capacity = 4
        self._check_stack_state(s, is_empty=False, is_full=True, length=4, capacity=4, top=4)

        # (1 2 3 _)
        self.assertEqual(s.pop(), 4)
        self._check_stack_state(s, is_empty=False, is_full=False, length=3, capacity=4, top=3)

        # (1 2 _ _)
        self.assertEqual(s.pop(), 3)
        self._check_stack_state(s, is_empty=False, is_full=False, length=2, capacity=4, top=2)

        # (1 2 7 _)
        s.push(7)
        self._check_stack_state(s, is_empty=False, is_full=False, length=3, capacity=4, top=7)

        # (1 _ _ _)
        self.assertEqual(s.pop(), 7)
        self.assertEqual(s.pop(), 2)
        self._check_stack_state(s, is_empty=False, is_full=False, length=1, capacity=4, top=1)

        # (_ _ _ _)
        self.assertEqual(s.pop(), 1)
        self._check_stack_state(s, is_empty=True, is_full=False, length=0, capacity=4)

        # (8 _ _ _)
        s.push(8)
        self._check_stack_state(s, is_empty=False, is_full=False, length=1, capacity=4, top=8)

        # (8)
        s.capacity = 1
        self.assertRaises(StackOverflowError, setattr, s, 'capacity', 0)
        self._check_stack_state(s, is_empty=False, is_full=True, length=1, capacity=1, top=8)

        # (_)
        self.assertEqual(s.pop(), 8)
        self._check_stack_state(s, is_empty=True, is_full=False, length=0, capacity=1)

        # ()
        s.capacity = 0
        self._check_stack_state(s, is_empty=True, is_full=True, length=0, capacity=0)
