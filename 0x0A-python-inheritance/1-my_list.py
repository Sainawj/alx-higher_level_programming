#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """
    Inherits from list and provides additional functionality.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
