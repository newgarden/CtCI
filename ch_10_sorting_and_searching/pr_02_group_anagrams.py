"""Group Anagrams.

Write a method to sort an array of strings so that all the anagrams are next to each other.
"""
import random
import unittest
from itertools import chain, combinations_with_replacement, groupby


def group_anagrams(lst: list[str]) -> None:
    """Sort an array of strings so that all anagrams are next to each other.

    Complexity: O(N * M * log(M)) time, O(N) additional space. Where M is a string length.

    :param lst: List to sort.
    """
    anagrams = {}
    for s in lst:
        digest = ''.join(sorted(s))
        if digest in anagrams:
            anagrams[digest].append(s)
        else:
            anagrams[digest] = [s]
    i = 0
    for v in anagrams.values():
        for s in v:
            lst[i] = s
            i += 1


class TestGroupAnagrams(unittest.TestCase):
    # Anagrams taken from https://www.litscape.com/words/anagram/4_word_anagrams.html
    anagrams = [
        ('o',),
        ('oh', 'ho'),
        ('ate', 'eat', 'eta', 'tea'),
        ('asps', 'pass', 'saps', 'spas'),
        ('limes', 'miles', 'slime', 'smile'),
        ('lameness',  'maleness', 'nameless', 'salesmen'),
    ]

    def generate_groups(self):
        for n_groups in range(0, 5):
            for group_sizes in combinations_with_replacement((1, 2, 3, 4), n_groups):
                groups = set()
                sample_anagrams = random.sample(self.anagrams, n_groups)
                for i, group_size in enumerate(group_sizes, 0):
                    group = random.choices(sample_anagrams[i], k=group_size)
                    groups.add(tuple(sorted(group)))
                yield(groups)

    def test_group_anagrams(self):
        random.seed(739485)
        for i in range(10):
            for groups in self.generate_groups():
                lst = list(chain.from_iterable(groups))
                random.shuffle(lst)
                with self.subTest(lst):
                    group_anagrams(lst)
                    groups_2 = set()
                    for _, group in groupby(lst, key=lambda s: sorted(s)):
                        groups_2.add(tuple(sorted(group)))
                    assert groups == groups_2
