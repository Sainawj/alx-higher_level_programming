#!/usr/bin/python3

"""Unit tests for Rectangle and Square classes."""


import unittest

from models.rectangle import Rectangle
from models.square import Square


class TestCreationMethods(unittest.TestCase):
    """Tests for the create method of Rectangle and Square classes."""

    def setUp(self):
        """Setup common objects for tests."""
        self.rect_params = {"width": 3, "height": 5, "x": 1, "y": 2, "id": 7}
        self.square_params = {"size": 3, "x": 5, "y": 1, "id": 7}

    def test_create_rectangle_original(self):
        """Test creation of a rectangle from its dictionary representation."""
        r1 = Rectangle(**self.rect_params)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_is(self):
        """Test if the created rectangle is not the same object."""
        r1 = Rectangle(**self.rect_params)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        """Test if the created rectangle is equal to the original."""
        r1 = Rectangle(**self.rect_params)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_create_square_original(self):
        """Test creation of a square from its dictionary representation."""
        s1 = Square(**self.square_params)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual("[Square] (7) 5/1 - 3", str(s1))

    def test_create_square_is(self):
        """Test if the created square is not the same object."""
        s1 = Square(**self.square_params)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsNot(s1, s2)

    def test_create_square_equals(self):
        """Test if the created square is equal to the original."""
        s1 = Square(**self.square_params)
        s2 = Square.create(**s1.to_dictionary())
        self.assertNotEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()
