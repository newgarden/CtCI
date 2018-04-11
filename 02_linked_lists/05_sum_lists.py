# -*- coding: utf-8 -*-
"""
Sum Lists.

Problem statement: You have two numbers represented by a linked list, where each node contains a
single digit. The digits are stored in reverse order, such that the 1'st digit is at the head of
the list. Write a function that adds the two numbers and returns the sum as a linked list.

Example:
    Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617 + 295.
    Output: 2 -> 1 -> 9. That is, 912.

Follow up: Suppose the digits are stored in forward order. Repeat the above problem.

Example:
    Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
    Output: 9 - > 1 -> 2. That is, 912.

"""
import unittest
from linked_list import ListNode, LinkedList


def reverse_list(lst):
    """
    Reverse linked list in place.

    Complexity: O(N) time, O(1) additional space.

    Args:
        lst (LinkedList): List to be reversed.

    """
    if not lst.head:
        return
    prev_node = lst.head
    node = prev_node.next
    while node:
        next_node = node.next
        node.next = prev_node
        prev_node = node
        node = next_node
    lst.head.next = None
    lst.head = prev_node


def sum_lists(lst1, lst2):
    """
    Sum lists in forward order.

    Complexity: O(N+M) time, O(M) space, where N and M a the lengths of the shortest and the
        longest lists respectively.

    This algorithm reverts both lists before and after calculating the sum. As a result it
    has side effect of temporarily changing arguments. On the other hand it allows us to avoid
    using additional memory.

    Args:
        lst1 (LinkedList): First operand.
        lst2 (LinkedList): Second operand.

    Returns:
        LinkedList: Sum of the two lists written in forward order.

    """
    reverse_list(lst1)
    reverse_list(lst2)

    node1 = lst1.head
    node2 = lst2.head
    carry = 0
    result = LinkedList()

    while node1 is not None or node2 is not None:
        new_node = ListNode(carry, result.head)

        if node1 is not None:
            new_node.value += node1.value
            node1 = node1.next
        if node2 is not None:
            new_node.value += node2.value
            node2 = node2.next

        if new_node.value > 9:
            carry = 1
            new_node.value = new_node.value % 10
        else:
            carry = 0

        result.head = new_node

    if carry:
        result.head = ListNode(1, result.head)

    reverse_list(lst1)
    reverse_list(lst2)

    return result


def sum_reversed_lists(lst1, lst2):
    """
    Sum lists in reverse order.

    Complexity: O(M) time, O(M) space, where N and M a the lengths of the shortest and the
        longest lists respectively.

   Args:
        lst1 (LinkedList): First operand.
        lst2 (LinkedList): Second operand.

    Returns:
        LinkedList: Sum of the two lists written in reverse order.

    """
    node1 = lst1.head
    node2 = lst2.head
    carry = 0
    result = LinkedList()
    result_tail = None

    while node1 is not None or node2 is not None:
        new_node = ListNode(carry)

        if node1 is not None:
            new_node.value += node1.value
            node1 = node1.next
        if node2 is not None:
            new_node.value += node2.value
            node2 = node2.next

        if new_node.value > 9:
            carry = 1
            new_node.value = new_node.value % 10
        else:
            carry = 0

        if result_tail:
            result_tail.next = new_node
            result_tail = new_node
        else:
            result.head = result_tail = new_node

    if carry:
        result_tail.next = ListNode(1)

    return result


class TestReverse(unittest.TestCase):
    data = [('', ''),
            ('a', 'a'),
            ('ab', 'ba'),
            ('abc', 'cba'),
            ('abcdef', 'fedcba')]

    def test_reverse_list(self):
        for input, output in self.data:
            lst = LinkedList(input)
            reverse_list(lst)
            self.assertEqual(lst, LinkedList(output))


class TestSumList(unittest.TestCase):
    data = [
        ((), (), ()),
        ((0,), (), (0,)),
        ((), (5,), (5,)),
        ((6, 1, 7), (2, 9, 5), (9, 1, 2)),
        ((8, 7, 9), (5, 8, 6), (1, 4, 6, 5)),
        ((9, 7, 8), (6, 8, 5), (1, 6, 6, 3)),
        ((9, 9, 9), (1,), (1, 0, 0, 0)),
        ((9, 9, 9), (9,), (1, 0, 0, 8)),
        ((1, 1, 1, 1), (4, 3, 2, 1), (5, 4, 3, 2)),
        ((3, 6, 7, 4), (3, 5, 1, 6), (7, 1, 9, 0)),
        ((1, 0, 2, 4), (3, 6), (1, 0, 6, 0)),
        ((2, 0, 4, 8), (6, 4), (2, 1, 1, 2))
    ]

    def test_sum_lists(self):
        for num1, num2, result in self.data:
            lst1 = LinkedList(num1)
            lst2 = LinkedList(num2)
            result_lst = LinkedList(result)
            self.assertEqual(sum_lists(lst1, lst2), result_lst)
            self.assertEqual(sum_lists(lst2, lst1), result_lst)

    def test_sum_reversed_lists(self):
        for num1, num2, result in self.data:
            lst1 = LinkedList(reversed(num1))
            lst2 = LinkedList(reversed(num2))
            result_lst = LinkedList(reversed(result))
            self.assertEqual(sum_reversed_lists(lst1, lst2), result_lst)
            self.assertEqual(sum_reversed_lists(lst2, lst1), result_lst)
