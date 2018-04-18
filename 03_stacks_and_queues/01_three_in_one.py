# -*- coding: utf-8 -*-
"""
Three in one.

Describe how you could use a single array to implement three stacks.

"""
from .stack import EmptyStackError, StackOverflowError


class Stack:
    """
    """

    def __init__(self, lst, min_index, max_index):
        self._lst = lst
        self._min_index = min_index
        self._max_index = max_index
        self._top = None

    def push(self, value):
        if self._top == self._max_index:
            raise StackOverflowError
        self._top += 1
        self._lst[self._top] = value

    def pop(self):
        if self._top is None:
            raise EmptyStackError

        value = self._top

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

    def __init__(self, capacity, length=3):
        self._lst = [None] * capacity * length
        self._stacks = []
        for i in range(length):
            self._stacks.append(Stack(self._lst, i * capacity, i * capacity + capacity - 1))

    def __getitem__(self, key):
        return self._stacks[key]
