#!/usr/bin/python3
"""
Contains the class MyInt
"""


class MyInt(int):
    """A rebellious version of an integer, perfect for opposite day!"""

    def __eq__(self, other):
        """Override == operator to act as !="""
        return int(self) != other

    def __ne__(self, other):
        """Override != operator to act as =="""
        return int(self) == other
