#!/usr/bin/python3
'''Module for BaseGeometry class.'''


class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        '''Method to compute this area.'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Method for validating the value.'''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
