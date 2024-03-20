#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = {}
    sum_unique = 0

    for num in my_list:
        if num not in unique_integers:
            unique_integers[num] = 1
            sum_unique += num

    return sum_unique

