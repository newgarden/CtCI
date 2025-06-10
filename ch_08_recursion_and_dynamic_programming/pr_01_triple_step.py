"""
Triple step

A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a
time. Implement a method to count how many possible ways the child can run up the stairs.

Problem depiction and test cases: ./images/problem-1-triple-step.svg

"""
import unittest


def triple_step(steps):
    """
    Count number of ways a child can run up the stairs.

    Counting is done using bottom-up dynamic programming in O(N) time and O(1) additional space.

    Args:
        steps (int): Number of steps in the stairs.

    Returns:
        int: Number of ways.

    """
    if steps < 1:
        return 0
    if steps == 1:
        return 1
    if steps == 2:
        return 2
    if steps == 3:
        return 4

    # Count ways for n steps, n - 1 steps and n - 2 steps
    n, n1, n2 = 7, 4, 2
    for i in range(5, steps + 1):
        n2, n1, n = n1, n, n2 + n1 + n

    return n


class TestTripleStep(unittest.TestCase):

    def test_triple_step(self):
        for steps, result in enumerate([0, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274]):
            self.assertEqual(triple_step(steps), result)
