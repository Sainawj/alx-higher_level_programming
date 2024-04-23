#!/usr/bin/python3

"""Defines unittests for models/square.py."""

import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Tests instantiation of the Square class."""

    def test_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_is_square(self):
        self.assertIsInstance(Square(10), Square)

    def test_invalid_args(self):
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_id_increment(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_positional_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(7, Square(10, 2, 2, 7).id)

    def test_size_property(self):
        self.assertEqual(5, Square(5, 2, 3, 9).size)

    def test_size_setter(self):
        s = Square(4, 1, 9, 2)
        s.size = 8
        self.assertEqual(8, s.size)

    def test_position_getters(self):
        s = Square(4, 1, 9, 2)
        self.assertEqual(0, s.x)
        self.assertEqual(0, s.y)


class TestSquareSizeValidation(unittest.TestCase):
    """Tests validation of Square size attribute."""

    def test_invalid_types(self):
        invalid_types = [None, "invalid", 5.5, complex(5), {"a": 1, "b": 2}, True, [1, 2, 3], {1, 2, 3},
                         (1, 2, 3), frozenset({1, 2, 3, 1}), range(5), b'Python', bytearray(b'abcdefg'),
                         memoryview(b'abcedfg'), float('inf'), float('nan')]
        for invalid_type in invalid_types:
            with self.subTest(invalid_type=invalid_type):
                with self.assertRaises(TypeError):
                    Square(invalid_type)

    def test_negative_and_zero_size(self):
        with self.assertRaises(ValueError):
            Square(-1, 2)
        with self.assertRaises(ValueError):
            Square(0, 2)


class TestSquarePositionValidation(unittest.TestCase):
    """Tests validation of Square position attributes."""

    def test_invalid_x(self):
        invalid_types = [None, "invalid", 5.5, complex(5), {"a": 1, "b": 2}, [1, 2, 3], {1, 2, 3},
                         (1, 2, 3), frozenset({1, 2, 3, 1}), range(5), b'Python', bytearray(b'abcdefg'),
                         memoryview(b'abcedfg'), float('inf'), float('nan')]
        for invalid_type in invalid_types:
            with self.subTest(invalid_type=invalid_type):
                with self.assertRaises(TypeError):
                    Square(1, invalid_type)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(3, 0, -1)


class TestSquareArea(unittest.TestCase):
    """Tests the area method of the Square class."""

    def test_area(self):
        self.assertEqual(100, Square(10, 0, 0, 1).area())

    def test_large_area(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_changed_attributes_area(self):
        s = Square(2, 0, 0, 1)
        s.size = 7
        self.assertEqual(49, s.area())


class TestSquareStringAndDisplay(unittest.TestCase):
    """Tests the __str__ and display methods of Square class."""

    def test_str_method(self):
        s = Square(4)
        self.assertEqual("[Square] ({}) 0/0 - 4\n".format(s.id), str(s))

    def test_display_method(self):
        s = Square(2, 0, 0, 9)
        capture = io.StringIO()
        sys.stdout = capture
        s.display()
        sys.stdout = sys.__stdout__
        self.assertEqual("##\n##\n", capture.getvalue())


if __name__ == "__main__":
    unittest.main()
