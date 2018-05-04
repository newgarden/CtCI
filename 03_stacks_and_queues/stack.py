# -*- coding: utf-8 -*-
import unittest


class StackError(Exception):
    """
    Base stack exception.
    """
    pass


class EmptyStackError(StackError):
    """
    Raised if peek() or pop() is attempted for an empty stack.
    """
    pass


class StackOverflowError(StackError):
    """
    Raised if a new element cannot be pushed to a stack because it has reached its full capacity.
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


class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = Stack()  # []

        self.assertRaises(EmptyStackError, stack.pop)
        self.assertRaises(EmptyStackError, stack.peek)
        self.assertIs(stack.is_empty(), True)

        stack.push(1)  # [1]

        self.assertEqual(stack.peek(), 1)
        self.assertIs(stack.is_empty(), False)

        item = stack.pop()  # []

        self.assertEqual(item, 1)
        self.assertRaises(EmptyStackError, stack.pop)
        self.assertRaises(EmptyStackError, stack.peek)
        self.assertIs(stack.is_empty(), True)

        stack.push(2)  # [2]
        stack.push(3)  # [2, 3]

        self.assertEqual(stack.peek(), 3)
        self.assertIs(stack.is_empty(), False)

        item = stack.pop()  # [2]

        self.assertEqual(item, 3)
        self.assertEqual(stack.peek(), 2)
        self.assertIs(stack.is_empty(), False)

        stack.push(4)  # [2, 4]
        stack.push(5)  # [2, 4, 5]

        self.assertEqual(stack.peek(), 5)
        self.assertIs(stack.is_empty(), False)

        item = stack.pop()  # [2, 4]

        self.assertEqual(item, 5)
        self.assertEqual(stack.peek(), 4)
        self.assertIs(stack.is_empty(), False)

        item = stack.pop()  # [2]

        self.assertEqual(item, 4)
        self.assertEqual(stack.peek(), 2)
        self.assertIs(stack.is_empty(), False)

        item = stack.pop()  # []

        self.assertEqual(item, 2)
        self.assertRaises(EmptyStackError, stack.pop)
        self.assertRaises(EmptyStackError, stack.peek)
        self.assertIs(stack.is_empty(), True)
