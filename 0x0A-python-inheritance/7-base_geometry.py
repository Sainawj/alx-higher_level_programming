#!/usr/bin/python3
'''Module for BaseGeometry class.'''


class BaseGeometry:
    '''A BaseGeometry class.'''
    def area(self):
        '''Method to compute this area.'''
        raise NotImplementedError('area() is not implemented')

    def integer_validator(self, name, value):
        '''Method for validating the value.'''
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
