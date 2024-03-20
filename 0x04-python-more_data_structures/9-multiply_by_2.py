#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiplied_dictionary = {}
    for key in a_dictionary:
        multiplied_dictionary[key] = a_dictionary[key] * 2
    return multiplied_dictionary

