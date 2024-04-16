#!/usr/bin/python3
'''Module for Square class.'''
from typing import Union
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''A subclass representing a square.'''
    def __init__(self, size: Union[int, float]):
        '''Constructor.'''
        super().__init__(size, size)

    def __str__(self) -> str:
        '''String representation method.'''
        return "[Square] {}/{}".format(self.width, self.height)
