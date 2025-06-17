"""
Loop Detection.

Given a circular linked list, implement an algorithm that returns the node at the beginning of
the loop.

Circular linked list is a (corrupt) linked list in which a node's next pointer points to an earlier
node, so as to make a loop in the linked list.

Example:
    Input: A -> B -> C - > D -> E -> C (the same C as earlier)
    Output: C

"""
import unittest

from .linked_list import LinkedList


def detect_loop(lst):
    """
    Find first loop node in a circular linked list.

    Complexity: O(N) time, O(1) additional space.

    Args:
        lst (LinkedList): List to check.

    Returns:
        ListNode: Node at the beginning of the loop. None if there is no loop.

    """
    if not lst.head:
        return None

    # Let's check if there is a loop, and find any node inside the loop.
    runner_1 = lst.head
    runner_2 = lst.head

    while True:
        runner_2 = runner_2.next
        if not runner_2:
            return None
        if runner_2 is runner_1:
            break

        runner_2 = runner_2.next
        if not runner_2:
            return None
        if runner_2 is runner_1:
            break

        runner_1 = runner_1.next

    # Find the number of nodes in the loop
    loop_length = 1
    while True:
        runner_2 = runner_2.next
        if runner_2 is runner_1:
            break
        loop_length += 1

    # Move runner_1 to the head and runner_2 loop_length steps forward from the head
    runner_1 = lst.head
    runner_2 = lst.head
    steps = 1
    while steps < loop_length:
        runner_2 = runner_2.next
        steps += 1

    # Move both runners until runner_1 reaches the beginning of the loop and runner_2 reaches the end.
    while runner_2.next is not runner_1:
        runner_2 = runner_2.next
        runner_1 = runner_1.next

    return runner_1


class TestLoopDetection(unittest.TestCase):

    def test_loop_detection(self):
        self.assertIsNone(detect_loop(LinkedList()))
        for i in range(1, 11):
            lst = LinkedList(range(i))
            self.assertIsNone(detect_loop(lst))
            for j in range(i):
                lst[i - 1].next = lst[j]
                self.assertIs(detect_loop(lst), lst[j])
