#!/usr/bin/python3

"""Module to find the max integer in a list"""


def max_integer(lst=[]):
    """Function to find and return the max integer in a list of integers.
    
    Args:
        lst (list, optional): A list of integers. Defaults to an empty list.

    Returns:
        int or None: The maximum integer in the list, or None if the list is empty.
    """
    if len(lst) == 0:
        return None
    
    result = lst[0]
    for num in lst:
        if num > result:
            result = num
    
    return result
