#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    def __str__(self):
        """Return string representation of Rectangle."""
        return f"Rectangle(width={self.width}, height={self.height})"

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the Rectangle."""
        return 2 * (self.__width + self.__height)

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

