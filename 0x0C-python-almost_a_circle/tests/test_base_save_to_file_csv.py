#!/usr/bin/python3

"""Unit tests for Base class's save_to_file_csv method."""


import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSaveToFileCSV(unittest.TestCase):
    """Tests for the save_to_file_csv method of Base class."""

    @classmethod
    def tearDownClass(cls):
        """Delete any created CSV files."""
        for file_name in ["Rectangle.csv", "Square.csv", "Base.csv"]:
            try:
                os.remove(file_name)
            except FileNotFoundError:
                pass

    def test_save_one_rectangle_csv(self):
        """Test saving one rectangle to CSV."""
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8", f.read())

    def test_save_two_rectangles_csv(self):
        """Test saving two rectangles to CSV."""
        r1 = Rectangle(10, 7, 2, 8, 5)
        r2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as f:
            self.assertTrue("5,10,7,2,8\n2,4,1,2,3", f.read())

    def test_save_one_square_csv(self):
        """Test saving one square to CSV."""
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_two_squares_csv(self):
        """Test saving two squares to CSV."""
        s1 = Square(10, 7, 2, 8)
        s2 = Square(8, 1, 2, 3)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2\n3,8,1,2", f.read())

    def test_save_to_file_csv_cls_name(self):
        """Test saving to CSV with the class name."""
        s = Square(10, 7, 2, 8)
        Base.save_to_file_csv([s])
        with open("Base.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_overwrite(self):
        """Test saving to CSV with overwrite."""
        s = Square(9, 2, 39, 2)
        Square.save_to_file_csv([s])
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as f:
            self.assertTrue("8,10,7,2", f.read())

    def test_save_to_file_csv_empty_list(self):
        """Test saving to CSV with an empty list."""
        Square.save_to_file_csv([])
        with open("Square.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_no_args(self):
        """Test saving to CSV with no arguments."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_save_to_file_csv_more_than_one_arg(self):
        """Test saving to CSV with more than one argument."""
        with self.assertRaises(TypeError):
            Square.save_to_file_csv([], 1)


if __name__ == "__main__":
    unittest.main()
