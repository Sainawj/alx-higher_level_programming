#!/usr/bin/python3
"""Python script to find a peak in an unsorted list of integers,
"""

"""
    THOUGHT PROCESS
        Since the list is unsorted, sorting it would require O(n log n) time,
            which is not efficient for this task.
        Iterating through the list and keeping track of the maximum
        value (brute force approach)
            results in a time complexity of O(n).

        Another approach involves iterating from both ends towards the middle,
            potentially reducing runtime to half.
            However, this method still operates in O(n) time.
"""


def find_peak(list_of_integers):
    """A brute-force implementation to find a peak in the list.
    """
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
