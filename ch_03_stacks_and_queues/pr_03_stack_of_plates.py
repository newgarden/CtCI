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

from .stacks import EmptyStackError


class SubStack(deque):
    """
    Sub-stack of SetOfStacks.

    It is implemented as a double-ended queue. Deque allows effective shifting of elements between
    sub-stacks to satisfy the follow-up problem. A plate can be taken from the top of a sub-stack
    and replaced by a plate taken from the bottom of the following sub-stack.

    Args:
         next_substack (SubStack): Pointer to next the sub-stack (the older one).

    """

    def __init__(self, next_substack=None):
        super(SubStack, self).__init__()
        self.next = next_substack


class SetOfStacks:
    """
    Implements stack of plates including follow up requirements.

    SetOfStacks is implemented as a linked list of double ended queues. The head of the list is
    the newest sub-stack in the set.

    Args:
        capacity (int): Capacity of the sub-stacks.

    """

    def __init__(self, capacity):
        self._capacity = capacity
        self._top = SubStack()
        self._length = 1

    def __len__(self):
        return self._length

    @property
    def capacity(self):
        """
        Capacity of the sub-stacks.
        """
        return self._capacity

    def pop(self):
        """
        Pop an element from the last (newest) sub-stack in O(1) time.

        Raises:
            EmptyStackError: If there is a single sub-stack which is empty.

        """
        if self._length == 1 and not len(self._top):
            raise EmptyStackError

        value = self._top.pop()

        if not len(self._top) and self._top.next:
            self._top = self._top.next
            self._length -= 1

        return value

    def push(self, value):
        """
        Push a new item to the set of stacks in O(1) time creating a new sub-stack if necessary.
        """
        if len(self._top) == self._capacity:
            self._top = SubStack(self._top)
            self._length += 1
        self._top.append(value)

    def peek(self):
        """
        Peek an element from the last (newest) sub-stack in O(1) time.

        Raises:
            EmptyStackError: If there is a single sub-stack which is empty.

        """
        if self._length == 1 and not len(self._top):
            raise EmptyStackError
        return self._top[-1]

    def is_empty(self):
        """
        Return True is set is empty, False otherwise.

        Set is considered empty if it consists of a single empty sub-stack.

        """
        return self._length == 1 and not len(self._top)

    def pop_at(self, i):
        """
        Pop an item from a specific sub-stack.

        When an item is popped from top of a sub-stack elements are shifted by popping the bottom
        element of the next sub-stack and pushing it to the top of current sub-stack. This operation
        is performed for all following sub-stacks.

        Since each sub-stack is a deque, taking items from the bottom and pushing them to the top
        is effective. For a set of N stacks the time complexity is O(N) no matter what sub-stack
        capacity is.

        Args:
            i (int): Index of sub-stack, zero based.

        Raises:
            IndexError: If index is out of range.
            EmptyStackError: If there is a single sub-stack which is empty.

        Examples:
            >>> s = SetOfStacks(3)
            >>> s.push(1), s.push(2), s.push(3), s.push(4), s.push(5)
            >>> s.push(6), s.push(7), s.push(8), s.push(9)
            >>> s.as_tuples()
            [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
            >>> s.pop_at(0)
            3
            >>> s.as_tuples()
            [(1, 2, 4), (5, 6, 7), (8, 9)]

        """
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
        """
        Represent the sub-stacks as a list of tuples.

        Useful for testing and inspecting the data structure.

        """
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

    def test_capacity_1(self):
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

    def test_capacity_2(self):
        s = SetOfStacks(2)
        self.assertEqual(s.capacity, 2)
        self._check_state(s, [()])

        s.push(0)
        self._check_state(s, [(0,)])

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

    def test_capacity_3(self):
        s = SetOfStacks(3)
        self.assertEqual(s.capacity, 3)
        self._check_state(s, [()])

        s.push(0)
        self._check_state(s, [(0,)])

        self.assertEqual(s.pop(), 0)
        self._check_state(s, [()])

        s.push(1)
        self._check_state(s, [(1,)])

        s.push(2)
        self._check_state(s, [(1, 2)])

        self.assertEqual(s.pop(), 2)
        self._check_state(s, [(1,)])

        self.assertEqual(s.pop_at(0), 1)
        self._check_state(s, [()])

        s.push(3)
        self._check_state(s, [(3,)])

        s.push(4)
        self._check_state(s, [(3, 4)])

        s.push(5)
        self._check_state(s, [(3, 4, 5)])

        s.push(6)
        self._check_state(s, [(3, 4, 5), (6,)])

        self.assertEqual(s.pop(), 6)
        self._check_state(s, [(3, 4, 5)])

        s.push(7)
        self._check_state(s, [(3, 4, 5), (7,)])

        s.push(8)
        self._check_state(s, [(3, 4, 5), (7, 8)])

        s.push(9)
        self._check_state(s, [(3, 4, 5), (7, 8, 9)])

        self.assertEqual(s.pop_at(0), 5)
        self._check_state(s, [(3, 4, 7), (8, 9)])

        self.assertEqual(s.pop(), 9)
        self._check_state(s, [(3, 4, 7), (8,)])

        s.push(10)
        self._check_state(s, [(3, 4, 7), (8, 10)])

        s.push(11)
        self._check_state(s, [(3, 4, 7), (8, 10, 11)])

        s.push(12)
        self._check_state(s, [(3, 4, 7), (8, 10, 11), (12,)])

        self.assertEqual(s.pop_at(2), 12)
        self._check_state(s, [(3, 4, 7), (8, 10, 11)])

        s.push(13)
        self._check_state(s, [(3, 4, 7), (8, 10, 11), (13,)])

        s.push(14)
        self._check_state(s, [(3, 4, 7), (8, 10, 11), (13, 14)])

        self.assertEqual(s.pop_at(1), 11)
        self._check_state(s, [(3, 4, 7), (8, 10, 13), (14,)])

        self.assertEqual(s.pop_at(1), 13)
        self._check_state(s, [(3, 4, 7), (8, 10, 14)])

        s.push(15)
        self._check_state(s, [(3, 4, 7), (8, 10, 14), (15,)])

        s.push(16)
        self._check_state(s, [(3, 4, 7), (8, 10, 14), (15, 16)])

        s.push(17)
        self._check_state(s, [(3, 4, 7), (8, 10, 14), (15, 16, 17)])

        s.push(18)
        self._check_state(s, [(3, 4, 7), (8, 10, 14), (15, 16, 17), (18,)])

        self.assertEqual(s.pop_at(0), 7)
        self._check_state(s, [(3, 4, 8), (10, 14, 15), (16, 17, 18)])

        s.push(19)
        self._check_state(s, [(3, 4, 8), (10, 14, 15), (16, 17, 18), (19,)])

        s.push(20)
        self._check_state(s, [(3, 4, 8), (10, 14, 15), (16, 17, 18), (19, 20)])

        s.push(21)
        self._check_state(s, [(3, 4, 8), (10, 14, 15), (16, 17, 18), (19, 20, 21)])

        self.assertRaises(IndexError, s.pop_at, 4)

        self.assertEqual(s.pop_at(0), 8)
        self._check_state(s, [(3, 4, 10), (14, 15, 16), (17, 18, 19), (20, 21)])

        self.assertEqual(s.pop_at(1), 16)
        self._check_state(s, [(3, 4, 10), (14, 15, 17), (18, 19, 20), (21,)])

        self.assertEqual(s.pop_at(2), 20)
        self._check_state(s, [(3, 4, 10), (14, 15, 17), (18, 19, 21)])

        self.assertEqual(s.pop(), 21)
        self._check_state(s, [(3, 4, 10), (14, 15, 17), (18, 19)])

        self.assertEqual(s.pop(), 19)
        self._check_state(s, [(3, 4, 10), (14, 15, 17), (18,)])

        self.assertEqual(s.pop_at(2), 18)
        self._check_state(s, [(3, 4, 10), (14, 15, 17)])

        self.assertEqual(s.pop_at(0), 10)
        self._check_state(s, [(3, 4, 14), (15, 17)])

        self.assertEqual(s.pop_at(0), 14)
        self._check_state(s, [(3, 4, 15), (17,)])

        self.assertEqual(s.pop_at(0), 15)
        self._check_state(s, [(3, 4, 17)])

        self.assertEqual(s.pop(), 17)
        self._check_state(s, [(3, 4)])

        self.assertEqual(s.pop(), 4)
        self._check_state(s, [(3,)])

        self.assertEqual(s.pop(), 3)
        self._check_state(s, [()])
