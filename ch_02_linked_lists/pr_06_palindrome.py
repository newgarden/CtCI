# -*- coding: utf-8 -*-
"""
Palindrome:

Problem statement: Implement a function to check if a linked list is a palindrome.

"""
import unittest
from .linked_list import LinkedList


def is_palindrome1(lst):
    """
    Checks if a linked list is a palindrome. Algorithm 1. Does not modify the list.

    Complexity: O(N) time, O(N) space.

    Args:
        lst (LinkedList): A linked list.

    Returns:
        bool: True if the list is a palindrome, False otherwise.

    """
    # Get the length of the list
    length = 0
    node = lst.head
    while node:
        length += 1
        node = node.next

    if length < 3:
        return True

    # Save the left half of the list in an array
    left_part = []
    node = lst.head
    for i in range(length // 2):
        left_part.append(node.value)
        node = node.next

    # If the length is odd ignore the middle node
    if length % 2:
        node = node.next

    # Go through the right half of the list comparing
    # each node with the corresponding node from the array.
    for i in range(length // 2):
        if left_part[-(i + 1)] != node.value:
            return False
        node = node.next

    return True


def is_palindrome2(lst):
    """
    Checks if a linked list is a palindrome. Algorithm 2. Reverses half of the list in place.

    Complexity: O(N) time, O(1) space.

    Args:
        lst (LinkedList): A linked list.

    Returns:
        bool: True if the list is a palindrome, False otherwise.

    """
    # Get the length of the list.
    length = 0
    node = lst.head
    while node:
        length += 1
        node = node.next

    if length < 3:
        return True

    # Go through the left half of the list with forward runner turning the next node pointers.
    prev_node = lst.head
    forward_runner = lst.head.next
    for i in range(length // 2 - 1):
        next_node = forward_runner.next
        forward_runner.next = prev_node
        prev_node = forward_runner
        forward_runner = next_node

    # If the length is odd ignore the middle node
    if length % 2:
        forward_runner = forward_runner.next

    # Go forward through the right half with the forward runner,
    # go back through the reversed left half with the backward runner,
    # compare runners' values.
    backward_runner = prev_node
    for i in range(length // 2):
        if backward_runner.value != forward_runner.value:
            return False
        forward_runner = forward_runner.next
        backward_runner = backward_runner.next

    return True


class TestPalindrome(unittest.TestCase):
    data = [
        ([], True),
        ('a', True),
        ('ab', True),
        ('abc', False), ('aba', True),
        ('abcd', False), ('abba', True),('abca', False), ('abbc', False),
        ('abcde', False), ('abcba', True), ('abcab', False), ('abcbc', False),
        ('abcdef', False), ('abccba', True), ('abccdb', False), ('abcdba', False), ('aaaaaa', True),
        ('abcdefg', False), ('abcdcba', True), ('aaabaaa', True), ('abacaba', True),
        ('jhklfkdsjkljkl', False), ('qwertyuiopasdfghjkllkjhgfdsapoiuytrewq', True)
    ]

    def test_palindrome1(self):
        for data in self.data:
            lst = LinkedList(data[0])
            self.assertEqual(is_palindrome1(lst), data[1])

    def test_palindrome2(self):
        for data in self.data:
            lst = LinkedList(data[0])
            self.assertEqual(is_palindrome2(lst), data[1])
