# -*- coding: utf-8 -*-
"""
Power set

Write a method to return all subsets of a set.

"""
import unittest


def power_set(iterable):
    """
    Generate power set for given iterable.

    Complexity: O(n*2^n) time and space.

    Args:
        iterable: Original set. Can be any iterable type.

    Returns:
        set: Set of frozen sets representing all subsets of the given iterable.

    """
    return _power_set_recurse(set(iterable))


def _power_set_recurse(s):
    """
    Recursively search for all subsets of given set.

    The initial set passed as argument is modified during the function execution. In order to avoid
    such side effects it is wrapped by power_set() function which works with copy of original set.

    Args:
        s (set): Original set.

    Returns:
        set: Set of frozen sets representing all subsets of the given iterable.

    """
    if not s:
        return {frozenset()}

    item = s.pop()

    subsets = _power_set_recurse(s)
    additional_subsets = set()

    for subset in subsets:
        additional_subsets.add(frozenset(list(subset) + [item]))

    return subsets | additional_subsets


def power_set_2(s):
    """
    Alternative implementation of power set using binary numbers approach.

    Complexity: O(n*2^n) time and space.

    Args:
        s (iterable): Original set. Can be any iterable type.

    Returns:
        set: Set of frozen sets representing all subsets of the given iterable.

    """
    l = list(s)
    result = set()

    for i in range(2**len(s)):
        subset_items = []
        bin_i = bin(i)
        for position in range(1, len(bin_i) - 1):
            if bin_i[-position] == '1':
                subset_items.append(l[-position])
        result.add(frozenset(subset_items))

    return result


class TestPowerSet(unittest.TestCase):
    data = [
        (set(), [[]]),
        ([1], [[], [1]]),
        ([1, 2], [[], [1], [2], [1, 2]]),
        ((1, 2, 3), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]),
        ('abcd', ['', 'a', 'b', 'c', 'd', 'ab', 'ac', 'ad', 'bc',
                  'bd', 'cd', 'abc', 'abd', 'acd', 'bcd', 'abcd']),
        ('abcde', ['', 'a', 'b', 'c', 'd', 'e', 'ab', 'ac', 'ad', 'ae', 'bc', 'bd', 'be', 'cd',
                   'ce', 'de', 'abc', 'abd', 'abe', 'acd', 'ace', 'ade', 'bcd', 'bce', 'bde',
                   'cde', 'abcd', 'abce', 'abde', 'acde', 'bcde', 'abcde']),
        ('abcdef', ['', 'a', 'b', 'c', 'd', 'e', 'f', 'ab', 'ac', 'ad', 'ae', 'af', 'bc', 'bd',
                    'be', 'bf', 'cd', 'ce', 'cf', 'de', 'df', 'ef', 'abc', 'abd', 'abe', 'abf',
                    'acd', 'ace', 'acf', 'ade', 'adf', 'aef', 'bcd', 'bce', 'bcf', 'bde', 'bdf',
                    'bef', 'cde', 'cdf', 'cef', 'def', 'abcd', 'abce', 'abcf', 'abde', 'abdf',
                    'abef', 'acde', 'acdf', 'acef', 'adef', 'bcde', 'bcdf', 'bcef', 'bdef',
                    'cdef', 'abcde', 'abcdf', 'abcef', 'abdef', 'acdef', 'bcdef', 'abcdef'])
    ]

    def test_power_set(self):
        for test_input, expected_output in self.data:
            self.assertEqual(power_set(test_input),
                             set([frozenset(s) for s in expected_output]))

    def test_power_set_2(self):
        for test_input, expected_output in self.data:
            self.assertEqual(power_set_2(test_input),
                             set([frozenset(s) for s in expected_output]))
