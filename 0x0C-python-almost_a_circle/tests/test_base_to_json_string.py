#!/usr/bin/python3

"""Unit tests for Base class's to_json_string method."""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestToJsonString(unittest.TestCase):
    """Tests for the to_json_string method of Base class."""

    def test_rectangle_type(self):
        """Test the return type for rectangles."""
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(str, type(Base.to_json_string([r.to_dictionary()])))

    def test_rectangle_one_dict(self):
        """Test the length of JSON string for one rectangle."""
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r.to_dictionary()])) == 53)

    def test_rectangle_two_dicts(self):
        """Test the length of JSON string for two rectangles."""
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        list_dicts = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 106)

    def test_square_type(self):
        """Test the return type for squares."""
        s = Square(10, 2, 3, 4)
        self.assertEqual(str, type(Base.to_json_string([s.to_dictionary()])))

    def test_square_one_dict(self):
        """Test the length of JSON string for one square."""
        s = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s.to_dictionary()])) == 39)

    def test_square_two_dicts(self):
        """Test the length of JSON string for two squares."""
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_empty_list(self):
        """Test JSON string for an empty list."""
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none(self):
        """Test JSON string for None."""
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_args(self):
        """Test JSON string with no arguments."""
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_than_one_arg(self):
        """Test JSON string with more than one argument."""
        with self.assertRaises(TypeError):
            Base.to_json_string([], 1)


if __name__ == "__main__":
    unittest.main()
