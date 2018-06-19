# -*- coding: utf-8 -*-
"""
Stack of Plates

Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in
real life, we would likely start a new stack when the previous stack exceeds some threshold.
Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of
several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).

FOLLOW UP
Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.

"""
from collections import deque
import unittest

from .stack import EmptyStackError


class SubStack(deque):

    def __init__(self, next_substack=None):
        super(SubStack, self).__init__()
        self.next = next_substack


class SetOfStacks:

    def __init__(self, capacity):
        self._capacity = capacity
        self._top = SubStack()
        self._length = 1

    def __len__(self):
        return self._length

    @property
    def capacity(self):
        return self._capacity

    def pop(self):
        if self._length == 1 and not len(self._top):
            raise EmptyStackError

        value = self._top.pop()

        if not len(self._top) and self._top.next:
            self._top = self._top.next
            self._length -= 1

        return value

    def push(self, value):
        if len(self._top) == self._capacity:
            self._top = SubStack(self._top)
            self._length += 1
        self._top.append(value)

    def peek(self):
        if self._length == 1 and not len(self._top):
            raise EmptyStackError
        return self._top[-1]

    def is_empty(self):
        return self._length == 1 and not len(self._top)

    def pop_at(self, i):
        if i < 0 or i > self._length - 1:
            raise IndexError

        if i == self._length - 1:
            return self.pop()

        current_index = self._length - 1
        current_substack = self._top
        carry = current_substack.popleft()
        while current_index > i + 1:
            current_substack = current_substack.next
            current_substack.append(carry)
            carry = current_substack.popleft()
            current_index -= 1
        current_substack = current_substack.next
        value = current_substack.pop()
        current_substack.append(carry)

        if not len(self._top) and self._top.next:
            self._top = self._top.next
            self._length -= 1

        return value

    def as_tuples(self):
        tuples = [None] * self._length
        current_substack = self._top
        for i in range(self._length - 1, -1, -1):
            tuples[i] = tuple(current_substack)
            current_substack = current_substack.next
        return tuples


class TestSetOfStacks(unittest.TestCase):

    def _check_state(self, stack, expected_state):
        self.assertEqual(stack.as_tuples(), expected_state)
        self.assertEqual(len(stack), len(expected_state))

        if expected_state == [()]:
            self.assertIs(stack.is_empty(), True)
            self.assertRaises(EmptyStackError, stack.pop),
            self.assertRaises(EmptyStackError, stack.peek)
            self.assertRaises(EmptyStackError, stack.pop_at, 0)
        else:
            self.assertIs(stack.is_empty(), False)
            self.assertEqual(stack.peek(), expected_state[-1][-1])

    def test_size_1(self):
        s = SetOfStacks(1)
        self.assertEqual(s.capacity, 1)
        self._check_state(s, [()])

        s.push(0)
        self._check_state(s, [(0,)])

        s.push(1)
        self._check_state(s, [(0,), (1,)])

        s.push(2)
        self._check_state(s, [(0,), (1,), (2,)])

        s.push(3)
        self._check_state(s, [(0,), (1,), (2,), (3,)])

        s.push(4)
        self._check_state(s, [(0,), (1,), (2,), (3,), (4,)])

        s.push(5)
        self._check_state(s, [(0,), (1,), (2,), (3,), (4,), (5,)])

        self.assertEqual(s.pop_at(3), 3)
        self._check_state(s, [(0,), (1,), (2,), (4,), (5,)])

        self.assertEqual(s.pop(), 5)
        self._check_state(s, [(0,), (1,), (2,), (4,)])

        self.assertEqual(s.pop_at(3), 4)
        self._check_state(s, [(0,), (1,), (2,)])

        self.assertRaises(IndexError, s.pop_at, 3)

        self.assertEqual(s.pop_at(0), 0)
        self._check_state(s, [(1,), (2,)])

        self.assertEqual(s.pop(), 2)
        self._check_state(s, [(1,)])

        self.assertEqual(s.pop(), 1)
        self._check_state(s, [()])

        s.push(6)
        self._check_state(s, [(6,)])

        s.push(7)
        self._check_state(s, [(6,), (7,)])

        self.assertEqual(s.pop(), 7)
        self._check_state(s, [(6,)])

        s.push(8)
        self._check_state(s, [(6,), (8,)])

        self.assertEqual(s.pop_at(0), 6)
        self._check_state(s, [(8,)])

        self.assertEqual(s.pop_at(0), 8)
        self._check_state(s, [()])

    def test_size_2(self):
        s = SetOfStacks(2)
        self.assertEqual(s.capacity, 2)
        self._check_state(s, [()])

        s.push(0)
        self._check_state(s, [(0, )])

        s.push(1)
        self._check_state(s, [(0, 1)])

        s.push(2)
        self._check_state(s, [(0, 1), (2,)])

        s.push(3)
        self._check_state(s, [(0, 1), (2, 3)])

        s.push(4)
        self._check_state(s, [(0, 1), (2, 3), (4,)])

        s.push(5)
        self._check_state(s, [(0, 1), (2, 3), (4, 5)])

        s.push(6)
        self._check_state(s, [(0, 1), (2, 3), (4, 5), (6,)])

        s.push(7)
        self._check_state(s, [(0, 1), (2, 3), (4, 5), (6, 7)])

        s.push(8)
        self._check_state(s, [(0, 1), (2, 3), (4, 5), (6, 7), (8,)])

        s.push(9)
        self._check_state(s, [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)])

        self.assertEqual(s.pop_at(0), 1)
        self._check_state(s, [(0, 2), (3, 4), (5, 6), (7, 8), (9,)])

        self.assertEqual(s.pop_at(1), 4)
        self._check_state(s, [(0, 2), (3, 5), (6, 7), (8, 9)])

        self.assertEqual(s.pop_at(2), 7)
        self._check_state(s, [(0, 2), (3, 5), (6, 8), (9,)])

        self.assertEqual(s.pop_at(3), 9)
        self._check_state(s, [(0, 2), (3, 5), (6, 8)])

        self.assertEqual(s.pop_at(2), 8)
        self._check_state(s, [(0, 2), (3, 5), (6,)])

        self.assertRaises(IndexError, s.pop_at, 3)

        self.assertEqual(s.pop(), 6)
        self._check_state(s, [(0, 2), (3, 5)])

        self.assertEqual(s.pop(), 5)
        self._check_state(s, [(0, 2), (3,)])

        self.assertEqual(s.pop_at(0), 2)
        self._check_state(s, [(0, 3)])

        self.assertEqual(s.pop_at(0), 3)
        self._check_state(s, [(0,)])

        s.push(10)
        self._check_state(s, [(0, 10)])

        s.push(11)
        self._check_state(s, [(0, 10), (11,)])

        self.assertEqual(s.pop(), 11)
        self._check_state(s, [(0, 10)])

        self.assertEqual(s.pop(), 10)
        self._check_state(s, [(0,)])

        self.assertEqual(s.pop(), 0)
        self._check_state(s, [()])

        s.push(12)
        self._check_state(s, [(12,)])
