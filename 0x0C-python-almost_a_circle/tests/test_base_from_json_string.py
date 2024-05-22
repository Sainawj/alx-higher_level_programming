#!/usr/bin/python3

"""Unit tests for Base class methods."""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestFromJsonString(unittest.TestCase):
    """Tests for the from_json_string method of Base class."""

    def test_list_type(self):
        """Test if the output is of type list."""
        list_input = [{"id": 89, "width": 10, "height": 4}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list, type(list_output))

    def test_one_rectangle(self):
        """Test deserialization of a single rectangle."""
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_two_rectangles(self):
        """Test deserialization of two rectangles."""
        list_input = [
            {"id": 89, "width": 10, "height": 4, "x": 7, "y": 8},
            {"id": 98, "width": 5, "height": 2, "x": 1, "y": 3},
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_one_square(self):
        """Test deserialization of a single square."""
        list_input = [{"id": 89, "size": 10, "height": 4}]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_two_squares(self):
        """Test deserialization of two squares."""
        list_input = [
            {"id": 89, "size": 10, "height": 4},
            {"id": 7, "size": 1, "height": 7}
        ]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_None_input(self):
        """Test deserialization with None input."""
        self.assertEqual([], Base.from_json_string(None))

    def test_empty_list_input(self):
        """Test deserialization with an empty list input."""
        self.assertEqual([], Base.from_json_string("[]"))

    def test_no_args_input(self):
        """Test deserialization with no arguments provided."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_more_than_one_arg_input(self):
        """Test deserialization with more than one argument provided."""
        with self.assertRaises(TypeError):
            Base.from_json_string([], 1)


if __name__ == "__main__":
    unittest.main()
