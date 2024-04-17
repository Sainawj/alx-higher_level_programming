#!/usr/bin/python3
"""function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line containing
    a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each line containing
            the search string.

    Returns:
        None
    """
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
