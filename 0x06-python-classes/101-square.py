#!/usr/bin/python3
"""Square class defination."""


class Square:
    """Defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square.
        """
        self._size = size
        self._position = position

    @property
    def size(self):
        """Getter and setter for the size attribute."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self):
        """Getter and setter for the position attribute."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for the position attribute."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """Calculates the area of the square."""
        return self._size ** 2

    def my_print(self):
        """Prints the square with '#' characters."""
        if self._size == 0:
            print("")
            return

        for _ in range(self._position[1]):
            print()
        for _ in range(self._size):
            print(" " * self._position[0], end="")
            print("#" * self._size)
