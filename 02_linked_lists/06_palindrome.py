# -*- coding: utf-8 -*-
"""
Palindrome:

Problem statement: Implement a function to check if a linked list is a palindrome.

Hints:#5, #13, #29, #61, #101

"""
import unittest
from linked_list import LinkedList


def is_palindrome1(lst):
    """
    Checks if a linked list is a palindrome using additional memory.

    Complexity: O(N) time, O(N) space.

    Args:
        lst (LinkedList): A linked list.

    Returns:
        bool: True if the list is a palindrome, False otherwise.

    """
    length = 0
    node = lst.head
    while node:
        length += 1
        node = node.next

    if length < 3:
        return True

    left_part = []
    node = lst.head
    for i in range(length // 2):
        left_part.append(node.value)
        node = node.next

    if length % 2:
        node = node.next

    for i in range(length // 2):
        if left_part[-(i + 1)] != node.value:
            return False
        node = node.next

    return True


def is_palindrome2(lst):
    """
    """
    pass


def is_palindrome3(lst):
    """
    """
    pass


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
