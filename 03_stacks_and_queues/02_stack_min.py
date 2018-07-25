# -*- coding: utf-8 -*-
"""
Stack Min

How would you design a stack which, in addition to push and pop, has a function min()
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

"""
import unittest
from .stacks import Stack, EmptyStackError


class MinStackItem:
    """
    Item of a MinStack.

    MinStack items are stored as a linked list like in a usual stack, but they have an additional
    pointer to the minimum stack element. This approach takes up O(N) extra memory but allows for
    O(1) access to the minimum element.

    Args:
        value: Item value.
        next_item (MinStackItem): Next item in a stack.

    Attributes:
        value: Item value.
        next (MinStackItem): Next item in a stack.
        min (MinStackItem): Item with the lowest value among current item and items added to a
            stack earlier.

    """
    __slots__ = ('value', 'next', 'min')

    def __init__(self, value, next_item=None):
        self.value = value
        self.next = next_item

        if not self.next or value < self.next.min.value:
            self.min = self
        else:
            self.min = self.next.min


class MinStack(Stack):
    """
    Stack which has additional method of getting the value of the minimum element.

    This is a subclass of Stack. It overrides push method which uses MinStackItem instead of
    StackItem and provides additional method for getting the value of the minimum element in O(1)
    time.

    """

    def push(self, value):
        self._top = MinStackItem(value, self._top)

    def peek_min(self):
        if not self._top:
            raise EmptyStackError
        return self._top.min.value


class TestMinStack(unittest.TestCase):

    def test_min_stack(self):
        stack = MinStack()  # []

        self.assertRaises(EmptyStackError, stack.pop)
        self.assertRaises(EmptyStackError, stack.peek)
        self.assertRaises(EmptyStackError, stack.peek_min)
        self.assertIs(stack.is_empty(), True)

        stack.push(8)  # [8]

        self.assertEqual(stack.peek(), 8)
        self.assertEqual(stack.peek_min(), 8)
        self.assertIs(stack.is_empty(), False)

        stack.push(16)  # [8, 16]

        self.assertEqual(stack.peek(), 16)
        self.assertEqual(stack.peek_min(), 8)

        stack.push(24)  # [8, 16, 24]

        self.assertEqual(stack.peek(), 24)
        self.assertEqual(stack.peek_min(), 8)

        stack.push(4)  # [8, 16, 24, 4]

        self.assertEqual(stack.peek(), 4)
        self.assertEqual(stack.peek_min(), 4)

        stack.push(12)  # [8, 16, 24, 4, 12]

        self.assertEqual(stack.peek(), 12)
        self.assertEqual(stack.peek_min(), 4)

        stack.push(2)  # [8, 16, 24, 4, 12, 2]

        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.peek_min(), 2)

        item = stack.pop()  # [8, 16, 24, 4, 12]

        self.assertEqual(item, 2)
        self.assertEqual(stack.peek(), 12)
        self.assertEqual(stack.peek_min(), 4)

        item = stack.pop()  # [8, 16, 24, 4]

        self.assertEqual(item, 12)
        self.assertEqual(stack.peek(), 4)
        self.assertEqual(stack.peek_min(), 4)

        item = stack.pop()  # [8, 16, 24]

        self.assertEqual(item, 4)
        self.assertEqual(stack.peek(), 24)
        self.assertEqual(stack.peek_min(), 8)

        item = stack.pop()  # [8, 16]

        self.assertEqual(item, 24)
        self.assertEqual(stack.peek(), 16)
        self.assertEqual(stack.peek_min(), 8)

        stack.push(2)  # [8, 16, 2]

        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.peek_min(), 2)

        stack.push(4)  # [8, 16, 2, 4]

        self.assertEqual(stack.peek(), 4)
        self.assertEqual(stack.peek_min(), 2)

        item = stack.pop()  # [8, 16, 2]

        self.assertEqual(item, 4)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.peek_min(), 2)

        item = stack.pop()  # [8, 16]

        self.assertEqual(item, 2)
        self.assertEqual(stack.peek(), 16)
        self.assertEqual(stack.peek_min(), 8)

        item = stack.pop()  # [8]

        self.assertEqual(item, 16)
        self.assertEqual(stack.peek(), 8)
        self.assertEqual(stack.peek_min(), 8)
        self.assertIs(stack.is_empty(), False)

        item = stack.pop()  # []

        self.assertEqual(item, 8)
        self.assertRaises(EmptyStackError, stack.pop)
        self.assertRaises(EmptyStackError, stack.peek)
        self.assertRaises(EmptyStackError, stack.peek_min)
        self.assertIs(stack.is_empty(), True)

        stack.push(5)  # [5]

        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.peek_min(), 5)
        self.assertIs(stack.is_empty(), False)

        item = stack.pop()  # []

        self.assertEqual(item, 5)
        self.assertRaises(EmptyStackError, stack.pop)
        self.assertRaises(EmptyStackError, stack.peek)
        self.assertRaises(EmptyStackError, stack.peek_min)
        self.assertIs(stack.is_empty(), True)

        stack.push(12)  # [12]

        self.assertEqual(stack.peek(), 12)
        self.assertEqual(stack.peek_min(), 12)
        self.assertIs(stack.is_empty(), False)

        stack.push(8)  # [12, 8]

        self.assertEqual(stack.peek(), 8)
        self.assertEqual(stack.peek_min(), 8)

        stack.push(4)  # [12, 8, 4]

        self.assertEqual(stack.peek(), 4)
        self.assertEqual(stack.peek_min(), 4)

        stack.push(6)  # [12, 8, 4, 6]

        self.assertEqual(stack.peek(), 6)
        self.assertEqual(stack.peek_min(), 4)

        item = stack.pop()  # [12, 8, 4]

        self.assertEqual(item, 6)
        self.assertEqual(stack.peek(), 4)
        self.assertEqual(stack.peek_min(), 4)

        item = stack.pop()  # [12, 8]

        self.assertEqual(item, 4)
        self.assertEqual(stack.peek(), 8)
        self.assertEqual(stack.peek_min(), 8)

        item = stack.pop()  # [12]

        self.assertEqual(item, 8)
        self.assertEqual(stack.peek(), 12)
        self.assertEqual(stack.peek_min(), 12)

        item = stack.pop()  # []

        self.assertEqual(item, 12)
        self.assertRaises(EmptyStackError, stack.pop)
        self.assertRaises(EmptyStackError, stack.peek)
        self.assertRaises(EmptyStackError, stack.peek_min)
        self.assertIs(stack.is_empty(), True)
