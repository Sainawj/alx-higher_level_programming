#!/usr/bin/python3


def append_write(filename="", text=""):
    '''Appends a string to a text file (UTF8) and returns the number of
    characters written.

    Args:
        filename (str): The name of the file to append to. Default is an
            empty string.
        text (str): The text to append to the file. Default is an empty
            string.

    Returns:
        int: The number of characters written to the file.
    '''
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars_written = file.write(text)
        return num_chars_written
