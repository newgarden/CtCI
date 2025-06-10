"""
Loop Detection

Given a circular linked list, implement an algorithm that returns the node at the beginning of
the loop.

Circular linked list is a linked list in which a node's next pointer points to an earlier
node, so as to make a loop in the linked list.

Example:
    Input: A -> B -> C - > D -> E -> C (the same C as earlier)
    Output: C

Hints: #50, #69, #83, #90

"""
import unittest
from .linked_list import LinkedList

def detect_loop(lst):
    """

    """
    if not lst.head:
        return None

    slow_runner = lst.head.next
    fast_runner = lst.head.next.next

    while True:
        if not fast_runner:
            return None

        slow_runner = slow_runner.next
        fast_runner = fast_runner.next

        if fast_runner is slow_runner:
            return fast_runner
        elif fast_runner is None:
            return None

        fast_runner = fast_runner.next


@unittest.skip('Problem is not solved yet.')
class TestLoopDetection(unittest.TestCase):

    def test_loop_detection(self):
        lst = LinkedList(range(40))
        for i in range(0, 40):
            lst[39].next = lst[i]
            print(i, detect_loop(lst).value)

            # print(i, detect_loop(lst).value)
