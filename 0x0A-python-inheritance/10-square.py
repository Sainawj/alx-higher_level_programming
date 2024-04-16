#!/usr/bin/python3
'''Module for Square class.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass representing a square.'''
    def __init__(self, size):
        '''Constructor.'''
        super().__init__(size, size)

    def __str__(self):
        '''String representation method.'''
        return "[Square] {}/{}".format(self.__size, self.__size)
