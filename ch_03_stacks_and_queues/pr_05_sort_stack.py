"""
Sort Stack.

Write a program to sort a stack such that the smallest items are on the top. You can use an
additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.

"""
import unittest

from .stacks import Stack


def sort_stack(stack):
    """
    Sort a stack using an auxiliary stack.

    My initial verbose solution.

    Complexity: O(N²) time, O(1) additional space.

    Args:
        stack (Stack): Stack to sort.

    """
    if stack.is_empty():
        return

    size = 0
    buffer = Stack()  # Second stack, the buffer

    # Move all elements from the first stack to the second, except for the biggest. Count the elements.
    maximum = stack.pop()
    while not stack.is_empty():
        value = stack.pop()
        size += 1
        if value > maximum:
            buffer.push(maximum)
            maximum = value
        else:
            buffer.push(value)
    stack.push(maximum)

    # Move elements between the stacks back and forth, until both contain half of the elements and sorted.
    # At the end the first stack will contain the bigger items sorted ascending from top to bottom.
    # The second stack will contain the smaller items sorted descending from top to bottom.
    while size:
        minimum = buffer.pop()
        size -= 1
        for i in range(size):
            value = buffer.pop()
            if value < minimum:
                stack.push(minimum)
                minimum = value
            else:
                stack.push(value)
        buffer.push(minimum)

        if not size:
            break

        maximum = stack.pop()
        size -= 1
        for i in range(size):
            value = stack.pop()
            if value > maximum:
                buffer.push(maximum)
                maximum = value
            else:
                buffer.push(value)
        stack.push(maximum)

    # Pop all elements from the buffer and push them into the first stack.
    while not buffer.is_empty():
        stack.push(buffer.pop())


def sort_stack_2(stack):
    """
    Sort a stack using an auxiliary stack.

    Better solution taken from the book.

    Complexity: O(N²) time, O(1) additional space.

    Args:
        stack (Stack): Stack to sort.

    """
    buffer = Stack()

    # Move all items from the stack to the buffer in sorted order, placing the biggest on the top.
    while not stack.is_empty():
        item = stack.pop()
        while not buffer.is_empty() and buffer.peek() > item:
            stack.push(buffer.pop())
        buffer.push(item)

    # Move all items from the buffer to the stack placing the smallest on the top.
    while not buffer.is_empty():
        stack.push(buffer.pop())


class TestSortStack(unittest.TestCase):
    data = [
        ([], []),
        ([5], [5]),
        ([4, 8], [4, 8]),
        ([8, 4], [4, 8]),
        ([4, 4], [4, 4]),
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([2, 3, 1], [1, 2, 3]),
        ([3, 3, 3], [3, 3, 3]),
        ([3, 2, 3], [2, 3, 3]),
        ([-2, 0, 2, 4], [-2, 0, 2, 4]),
        ([4, 2, 0, -2], [-2, 0, 2, 4]),
        ([0, 2, 4, -2], [-2, 0, 2, 4]),
        ([0, 4, 4, -2], [-2, 0, 4, 4]),
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([-32, -16, -8, -4, -2], [-32, -16, -8, -4, -2]),
        ([-2, -4, -8, -16, -32], [-32, -16, -8, -4, -2]),
        ([-32, -16, -2, -4, -8], [-32, -16, -8, -4, -2]),
        ([-16, -16, -2, -8, -8], [-16, -16, -8, -8, -2]),
        ([-4, -4, 1, 6, 9, 9], [-4, -4, 1, 6, 9, 9]),
        ([9, 9, 6, 1, -4, -4], [-4, -4, 1, 6, 9, 9]),
        ([9, -4, 6, 9, 1, -4], [-4, -4, 1, 6, 9, 9]),
        ([0.1, 0.4, 0.2, 0.3, 0.1, 0, 0.1], [0, 0.1, 0.1, 0.1, 0.2, 0.3, 0.4]),
        (['a', 'd', 'd', 'h', 'e', 'h', 'c', 'b'], ['a', 'b', 'c', 'd', 'd', 'e', 'h', 'h']),
        ([0, -1, -2, -3, 0, 1, 2, 3, 0], [-3, -2, -1, 0, 0, 0, 1, 2, 3]),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([6, 7, 5, 8, 4, 3, 9, 2, 0, 1], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
    ]

    def create_stack(self, values):
        stack = Stack()
        for value in values:
            stack.push(value)
        return stack

    def stack_to_list(self, stack):
        l = []
        while not stack.is_empty():
            l.append(stack.pop())
        return l

    def test_sort_stack(self):
        for values, sorted_values in self.data:
            with self.subTest(values=values):
                stack = self.create_stack(values)
                sort_stack(stack)
                self.assertEqual(self.stack_to_list(stack), sorted_values)

    def test_sort_stack_2(self):
        for values, sorted_values in self.data:
            with self.subTest(values=values):
                stack = self.create_stack(values)
                sort_stack_2(stack)
                self.assertEqual(self.stack_to_list(stack), sorted_values)
