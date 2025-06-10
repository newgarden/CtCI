"""
Three in one

Describe how you could use a single array to implement three stacks.

"""
import unittest
from .stacks import EmptyStackError, StackOverflowError


class StackArrayItem:
    """
    Stack which occupies a part of an array.

    This class is not supposed to be used by itself but as a part of a StackArray.

    Args:
        lst (list): List which stores stack items.
        min_index (int): Start of list section occupied by the stack.
        max_index (int): End of list section occupied by the stack.

    """

    def __init__(self, lst, min_index, max_index):
        self._lst = lst
        self._min_index = min_index
        self._max_index = max_index
        self._top = None

    def push(self, value):
        if self._top == self._max_index:
            raise StackOverflowError

        if self._top is None:
            self._top = self._min_index
        else:
            self._top += 1

        self._lst[self._top] = value

    def pop(self):
        if self._top is None:
            raise EmptyStackError

        value = self._lst[self._top]

        if self._top == self._min_index:
            self._top = None
        else:
            self._top -= 1

        return value

    def peek(self):
        if self._top is None:
            raise EmptyStackError
        return self._lst[self._top]

    def is_empty(self):
        return self._top is None


class StackArray:
    """
    Data structure which uses a single list to store multiple stacks.

    This is a container of StackArrayItem objects that share a single list for storage. Each stack
    can be accessed by index.

    Args:
        capacity (int): Stack size, equal for all.
        length (int): Number of stacks in StackArray.

    """

    def __init__(self, capacity, length=3):
        self._length = length
        self._lst = [None] * capacity * length
        self._stacks = []
        for i in range(length):
            self._stacks.append(
                StackArrayItem(self._lst, i * capacity, i * capacity + capacity - 1)
            )

    def __getitem__(self, key):
        return self._stacks[key]

    def __len__(self):
        return self._length


class TestStackArray(unittest.TestCase):

    def test_stack_array_4x1(self):
        # (_ _ _ _)
        #   empty
        stack_array = StackArray(4, 1)

        self.assertEqual(len(stack_array), 1)
        self.assertRaises(IndexError, lambda: stack_array[1])
        self.assertIs(type(stack_array[0]), StackArrayItem)
        self.assertRaises(EmptyStackError, stack_array[0].pop)
        self.assertRaises(EmptyStackError, stack_array[0].peek)
        self.assertIs(stack_array[0].is_empty(), True)

        # (1 _ _ _)
        #  ^
        stack_array[0].push(1)
        self.assertEqual(stack_array[0].peek(), 1)
        self.assertIs(stack_array[0].is_empty(), False)

        # (1 _ _ _)
        #   empty
        self.assertEqual(stack_array[0].pop(), 1)
        self.assertRaises(EmptyStackError, stack_array[0].pop)
        self.assertRaises(EmptyStackError, stack_array[0].peek)
        self.assertIs(stack_array[0].is_empty(), True)

        # (2 3 4 _)
        #      ^
        stack_array[0].push(2)
        stack_array[0].push(3)
        stack_array[0].push(4)
        self.assertEqual(stack_array[0].peek(), 4)
        self.assertIs(stack_array[0].is_empty(), False)

        # (2 3 4 5)
        #        ^
        stack_array[0].push(5)
        self.assertRaises(StackOverflowError, stack_array[0].push, 6)
        self.assertEqual(stack_array[0].peek(), 5)
        self.assertIs(stack_array[0].is_empty(), False)

        # (2 3 4 5)
        #      ^
        self.assertEqual(stack_array[0].pop(), 5)
        self.assertEqual(stack_array[0].peek(), 4)
        self.assertIs(stack_array[0].is_empty(), False)

        # (2 3 4 5)
        #   empty
        self.assertEqual(stack_array[0].pop(), 4)
        self.assertEqual(stack_array[0].pop(), 3)
        self.assertEqual(stack_array[0].pop(), 2)
        self.assertRaises(EmptyStackError, stack_array[0].pop)
        self.assertRaises(EmptyStackError, stack_array[0].peek)
        self.assertIs(stack_array[0].is_empty(), True)

    def test_stack_array_1x2(self):
        # (_) (_)
        #  e   e
        stack_array = StackArray(1, 2)
        self.assertEqual(len(stack_array), 2)
        self.assertRaises(IndexError, lambda: stack_array[2])

        for i in range(2):
            self.assertIs(type(stack_array[i]), StackArrayItem)
            self.assertRaises(EmptyStackError, stack_array[i].pop)
            self.assertRaises(EmptyStackError, stack_array[i].peek)
            self.assertIs(stack_array[i].is_empty(), True)

        # (1) (_)
        #  ^   e
        stack_array[0].push(1)
        self.assertRaises(StackOverflowError, stack_array[0].push, 2)
        self.assertEqual(stack_array[0].peek(), 1)
        self.assertIs(stack_array[0].is_empty(), False)
        self.assertRaises(EmptyStackError, stack_array[1].pop)
        self.assertRaises(EmptyStackError, stack_array[1].peek)
        self.assertIs(stack_array[1].is_empty(), True)

        # (1) (a)
        #  e   ^
        stack_array[1].push('a')
        self.assertEqual(stack_array[0].pop(), 1)
        self.assertRaises(EmptyStackError, stack_array[0].pop)
        self.assertRaises(EmptyStackError, stack_array[0].peek)
        self.assertIs(stack_array[0].is_empty(), True)
        self.assertRaises(StackOverflowError, stack_array[1].push, 'b')
        self.assertEqual(stack_array[1].peek(), 'a')
        self.assertIs(stack_array[1].is_empty(), False)

        # (2) (a)
        #  ^   e
        stack_array[0].push(2)
        stack_array[1].pop()
        self.assertRaises(StackOverflowError, stack_array[0].push, 3)
        self.assertEqual(stack_array[0].peek(), 2)
        self.assertIs(stack_array[0].is_empty(), False)
        self.assertRaises(EmptyStackError, stack_array[1].pop)
        self.assertRaises(EmptyStackError, stack_array[1].peek)
        self.assertIs(stack_array[1].is_empty(), True)

    def test_stack_array_3x3(self):
        # (_ _ _) (_ _ _) (_ _ _)
        #  empty   empty   empty
        stack_array = StackArray(3, 3)

        self.assertEqual(len(stack_array), 3)
        self.assertRaises(IndexError, lambda: stack_array[len(stack_array)])

        for i in range(len(stack_array)):
            self.assertIs(type(stack_array[i]), StackArrayItem)
            self.assertIs(stack_array[i].is_empty(), True)
            self.assertRaises(EmptyStackError, stack_array[i].peek)
            self.assertRaises(EmptyStackError, stack_array[i].pop)

        # (1 _ _) (a _ _) (@ _ _)
        #  ^       ^       ^
        stack_array[0].push(1)
        stack_array[1].push('a')
        stack_array[2].push('@')

        self.assertEqual(stack_array[0].peek(), 1)
        self.assertEqual(stack_array[1].peek(), 'a')
        self.assertEqual(stack_array[2].peek(), '@')
        self.assertIs(stack_array[0].is_empty(), False)
        self.assertIs(stack_array[1].is_empty(), False)
        self.assertIs(stack_array[2].is_empty(), False)

        # (1 2 _) (a b _) (@ _ _)
        #    ^       ^     empty
        stack_array[0].push(2)
        stack_array[1].push('b')
        item2 = stack_array[2].pop()

        self.assertEqual(stack_array[0].peek(), 2)
        self.assertEqual(stack_array[1].peek(), 'b')
        self.assertEqual(item2, '@')
        self.assertIs(stack_array[0].is_empty(), False)
        self.assertIs(stack_array[1].is_empty(), False)
        self.assertIs(stack_array[2].is_empty(), True)
        self.assertRaises(EmptyStackError, stack_array[2].peek)
        self.assertRaises(EmptyStackError, stack_array[2].pop)

        # (1 2 3) (a b _) (# _ _)
        #      ^   ^       ^
        stack_array[0].push(3)
        item1 = stack_array[1].pop()
        stack_array[2].push('#')

        self.assertEqual(stack_array[0].peek(), 3)
        self.assertEqual(stack_array[1].peek(), 'a')
        self.assertEqual(stack_array[2].peek(), '#')
        self.assertEqual(item1, 'b')
        self.assertIs(stack_array[0].is_empty(), False)
        self.assertIs(stack_array[1].is_empty(), False)
        self.assertIs(stack_array[2].is_empty(), False)
        self.assertRaises(StackOverflowError, stack_array[0].push, 4)

        # (1 2 3) (a c _) (# $ _)
        #    ^       ^       ^
        item0 = stack_array[0].pop()
        stack_array[1].push('c')
        stack_array[2].push('$')

        self.assertEqual(stack_array[0].peek(), 2)
        self.assertEqual(stack_array[1].peek(), 'c')
        self.assertEqual(stack_array[2].peek(), '$')
        self.assertEqual(item0, 3)

        # (1 2 3) (a c d) (# $ &)
        #  ^           ^       ^
        item0 = stack_array[0].pop()
        stack_array[1].push('d')
        stack_array[2].push('&')

        self.assertEqual(stack_array[0].peek(), 1)
        self.assertEqual(stack_array[1].peek(), 'd')
        self.assertEqual(stack_array[2].peek(), '&')
        self.assertEqual(item0, 2)
        self.assertIs(stack_array[0].is_empty(), False)
        self.assertRaises(StackOverflowError, stack_array[1].push, 'e')
        self.assertRaises(StackOverflowError, stack_array[2].push, '%')

        # (1 2 3) (a c d) (# $ &)
        #  empty     ^       ^
        item0 = stack_array[0].pop()
        item1 = stack_array[1].pop()
        item2 = stack_array[2].pop()

        self.assertEqual(stack_array[1].peek(), 'c')
        self.assertEqual(stack_array[2].peek(), '$')
        self.assertEqual(item0, 1)
        self.assertEqual(item1, 'd')
        self.assertEqual(item2, '&')
        self.assertIs(stack_array[0].is_empty(), True)
        self.assertIs(stack_array[1].is_empty(), False)
        self.assertIs(stack_array[2].is_empty(), False)
        self.assertRaises(EmptyStackError, stack_array[0].pop)

        # (4 2 3) (a c d) (# $ &)
        #  ^       ^       ^
        stack_array[0].push(4)
        item1 = stack_array[1].pop()
        item2 = stack_array[2].pop()

        self.assertEqual(stack_array[0].peek(), 4)
        self.assertEqual(stack_array[1].peek(), 'a')
        self.assertEqual(stack_array[2].peek(), '#')
        self.assertEqual(item1, 'c')
        self.assertEqual(item2, '$')
        self.assertIs(stack_array[0].is_empty(), False)
        self.assertIs(stack_array[1].is_empty(), False)
        self.assertIs(stack_array[2].is_empty(), False)

        # (4 5 3) (a c d) (# * &)
        #    ^     empty     ^
        stack_array[0].push(5)
        item1 = stack_array[1].pop()
        stack_array[2].push('*')

        self.assertEqual(stack_array[0].peek(), 5)
        self.assertEqual(stack_array[2].peek(), '*')
        self.assertEqual(item1, 'a')
        self.assertIs(stack_array[1].is_empty(), True)
        self.assertRaises(EmptyStackError, stack_array[1].peek)
        self.assertRaises(EmptyStackError, stack_array[1].pop)

        # (4 5 3) (e c d) (# * &)
        #    ^     ^       ^
        stack_array[1].push('e')
        item2 = stack_array[2].pop()

        self.assertEqual(stack_array[1].peek(), 'e')
        self.assertEqual(stack_array[2].peek(), '#')
        self.assertEqual(item2, '*')
        self.assertIs(stack_array[1].is_empty(), False)
        self.assertIs(stack_array[2].is_empty(), False)

        # (4 5 3) (e c d) (# * &)
        #    ^     ^       empty
        item2 = stack_array[2].pop()

        self.assertEqual(stack_array[0].peek(), 5)
        self.assertEqual(stack_array[1].peek(), 'e')
        self.assertEqual(item2, '#')
        self.assertIs(stack_array[0].is_empty(), False)
        self.assertIs(stack_array[1].is_empty(), False)
        self.assertIs(stack_array[2].is_empty(), True)
        self.assertRaises(EmptyStackError, stack_array[2].peek)
        self.assertRaises(EmptyStackError, stack_array[2].pop)
