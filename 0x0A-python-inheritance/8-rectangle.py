#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
===================================
module with class Rectangle
===================================
"""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method for calculating the area"""
        return self.__width * self.__height
