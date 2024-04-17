#!/usr/bin/python3
"""Funtion:  writes a string to a text file (UTF8)
    returns the number of characters written"""


def write_file(filename="", text=""):
    """Writes a string to a text file

    Returns: number of characters written.
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
