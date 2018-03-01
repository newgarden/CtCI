# -*- coding: utf-8 -*-
from linked_list import LinkedList

def get_kth_to_last(lst, k):
    """
    """
    runner = lst.head
    for i in range(k):
        if not runner:
            return None
        runner = runner.next

    result = lst.head
    while runner:
        print('Here2')
        runner = runner.next
        result = result.next

    return result

lst = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(get_kth_to_last(lst, -1))
