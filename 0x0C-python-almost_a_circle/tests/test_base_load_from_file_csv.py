#!/usr/bin/python3

"""Unit tests for Base class's load_from_file_csv method."""


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestLoadFromFileCSV(unittest.TestCase):
    """Tests for the load_from_file_csv method of Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created CSV files."""
        for file_name in ["Rectangle.csv", "Square.csv"]:
            try:
                os.remove(file_name)
            except FileNotFoundError:
                pass

    def test_load_first_rectangle_csv(self):
        """Test loading the first rectangle from CSV."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file_csv([r1])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_second_rectangle_csv(self):
        """Test loading the second rectangle from CSV."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_rectangle_types_csv(self):
        """Test loading rectangles from CSV and checking their types."""
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in output))

    def test_load_first_square_csv(self):
        """Test loading the first square from CSV."""
        s1 = Square(5, 1, 3, 3)
        Square.save_to_file_csv([s1])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(list_squares_output[0]))

    def test_load_second_square_csv(self):
        """Test loading the second square from CSV."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_squares_output[1]))

    def test_load_square_types_csv(self):
        """Test loading squares from CSV and checking their types."""
        s1 = Square(5, 1, 3, 3)
        s2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Square) for obj in output))

    def test_load_no_file_csv(self):
        """Test loading from CSV when the file doesn't exist."""
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_load_more_than_one_arg_csv(self):
        """Test loading from CSV with more than one argument."""
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
