# -*- coding: utf-8 -*-
"""
Stack implementation.
"""
import unittest


class StackError(Exception):
    """
    Base stack exception.
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


class StackItem:
    """
    Item of a linked list that constitutes a stack, used internally by Stack class.

    Args:
        value: Value of stack item.
        next_item (StackItem): Next item in the stack (under the current one).

    Attributes:
        value: Value of stack item.
        next: (StackItem): Next item in the stack (under the current one).

    """
    __slots__ = ('value', 'next')

    def __init__(self, value, next_item=None):
        self.value = value
        self.next = next_item


class Stack:
    """
    Stack implementation based on linked list.
    """

    def __init__(self):
        self._top = None

    def push(self, value):
        """
        Push value to the stack.
        """
        self._top = StackItem(value, self._top)

    def pop(self):
        """
        Remove top item from the stack and return its value.

        Raises:
            EmptyStackError: If stack is empty.

        """
        if not self._top:
            raise EmptyStackError
        value = self._top.value
        self._top = self._top.next
        return value

    def peek(self):
        """
        Get the value of top item without removing it.

        Raises:
            EmptyStackError: If stack is empty.

        """
        if self._top is None:
            raise EmptyStackError
        return self._top.value

    def is_empty(self):
        """
        Return True if stack is empty, False otherwise.
        """
        return self._top is None


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def _check_stack_state(self, is_empty, top=None):
        self.assertIs(self.stack.is_empty(), is_empty)
        if is_empty:
            self.assertRaises(EmptyStackError, self.stack.pop)
            self.assertRaises(EmptyStackError, self.stack.peek)
        else:
            self.assertEqual(self.stack.peek(), top)

    def test_stack(self):
        s = self.stack
        self._check_stack_state(is_empty=True)          # []

        s.push(1)
        self._check_stack_state(is_empty=False, top=1)  # [1]

        self.assertEqual(s.pop(), 1)
        self._check_stack_state(is_empty=True)          # []

        s.push(2)
        self._check_stack_state(is_empty=False, top=2)  # [2]

        s.push(3)
        self._check_stack_state(is_empty=False, top=3)  # [2 3]

        self.assertEqual(s.pop(), 3)
        self._check_stack_state(is_empty=False, top=2)  # [2]

        s.push(4)
        self._check_stack_state(is_empty=False, top=4)  # [2 4]

        s.push(5)
        self._check_stack_state(is_empty=False, top=5)  # [2 4 5]

        self.assertEqual(s.pop(), 5)
        self._check_stack_state(is_empty=False, top=4)  # [2 4]

        self.assertEqual(s.pop(), 4)
        self._check_stack_state(is_empty=False, top=2)  # [2]

        self.assertEqual(s.pop(), 2)
        self._check_stack_state(is_empty=True)          # []
