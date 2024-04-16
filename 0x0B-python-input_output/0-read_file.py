#!/usr/bin/python3
'''Module for reading a text file and printing it to stdout.'''

def read_file(filename=""):
    '''Reads a text file and prints its content to stdout.

    Args:
        filename (str): The name of the file to be read. Default is an empty string.

    Returns:
        None
    '''
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            print(line, end='')
