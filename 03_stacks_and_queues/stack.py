# -*- coding: utf-8 -*-


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
