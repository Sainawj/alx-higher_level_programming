#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_elements = set(set_1)
    unique_elements.update(set_2)
    common_elements = set(set_1).intersection(set_2)
    return unique_elements - common_elements
