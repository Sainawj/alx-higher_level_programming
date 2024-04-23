#!/usr/bin/python3

"""Defines unittests for models/square.py.
Unittest classes:
    TestSquare_instantiation - line 24
    TestSquare_size - line 88
    TestSquare_x - line 166
    TestSquare_y - line 238
    TestSquare_order_of_initialization - line 306
    TestSquare_area - line 322
    TestSquare_stdout - line 343
    TestSquare_update_args - line 426
    TestSquare_update_kwargs - line 538
    TestSquare_to_dictionary - 640
"""


import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquareInstantiation(unittest.TestCase):
    """Tests instantiation of the Square class."""

    def setUp(self):
        self.s = Square(10, 2, 3, 4)

    def test_is_base(self):
        self.assertIsInstance(self.s, Base)

    def test_is_square(self):
        self.assertIsInstance(self.s, Square)

    def test_id_increment(self):
        s2 = Square(11)
        self.assertEqual(self.s.id + 1, s2.id)

    def test_arguments(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id + 1, s2.id)

        s1 = Square(10, 2, 2)
        s2 = Square(2, 2, 10)
        self.assertEqual(s1.id + 1, s2.id)

        s = Square(10, 2, 2, 7)
        self.assertEqual(7, s.id)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(self.s.__size)

    def test_size_getter(self):
        self.assertEqual(10, self.s.size)

    def test_size_setter(self):
        self.s.size = 8
        self.assertEqual(8, self.s.size)

    def test_width_getter(self):
        self.assertEqual(10, self.s.width)

    def test_height_getter(self):
        self.assertEqual(10, self.s.height)

    def test_x_getter(self):
        self.assertEqual(2, self.s.x)

    def test_y_getter(self):
        self.assertEqual(3, self.s.y)


class TestSquareSize(unittest.TestCase):
    """Tests size initialization of the Square class."""

    def test_invalid_size_types(self):
        invalid_types = [None, "invalid", 5.5, complex(5), {"a": 1, "b": 2}, True, [1, 2, 3], {1, 2, 3},
                         (1, 2, 3), frozenset({1, 2, 3, 1}), range(5), b'Python', bytearray(b'abcdefg'),
                         memoryview(b'abcdefg'), float('inf'), float('nan')]
        for size in invalid_types:
            with self.subTest(size=size):
                with self.assertRaises(TypeError):
                    Square(size)

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            Square(-1)

    def test_zero_size(self):
        with self.assertRaises(ValueError):
            Square(0)


class TestSquareX(unittest.TestCase):
    """Tests initialization of Square x attribute."""

    def test_invalid_x_types(self):
        invalid_types = [None, "invalid", 5.5, complex(5), {"a": 1, "b": 2}, [1, 2, 3], {1, 2, 3},
                         (1, 2, 3), frozenset({1, 2, 3, 1}), range(5), b'Python', bytearray(b'abcdefg'),
                         memoryview(b'abcedfg'), float('inf'), float('nan')]
        for x in invalid_types:
            with self.subTest(x=x):
                with self.assertRaises(TypeError):
                    Square(1, x)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            Square(5, -1, 0)


class TestSquareY(unittest.TestCase):
    """Tests initialization of Square y attribute."""

    def test_invalid_y_types(self):
        invalid_types = [None, "invalid", 5.5, complex(5), {"a": 1, "b": 2}, [1, 2, 3], {1, 2, 3},
                         (1, 2, 3), frozenset({1, 2, 3, 1}), range(5), b'Python', bytearray(b'abcdefg'),
                         memoryview(b'abcedfg'), float('inf'), float('nan')]
        for y in invalid_types:
            with self.subTest(y=y):
                with self.assertRaises(TypeError):
                    Square(1, 1, y)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            Square(3, 0, -1)


class TestSquareOrderOfInitialization(unittest.TestCase):
    """Tests order of Square attribute initialization."""

    def test_size_before_x(self):
        with self.assertRaises(TypeError):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        with self.assertRaises(TypeError):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        with self.assertRaises(TypeError):
            Square(1, "invalid x", "invalid y")


class TestSquareArea(unittest.TestCase):
    """Tests the area method of the Square class."""

    def test_area_small(self):
        s = Square(10, 0, 0, 1)
        self.assertEqual(100, s.area())

    def test_area_large(self):
        s = Square(999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999999998000000000000000001, s.area())

    def test_area_changed_attributes(self):
        s = Square(2, 0, 0, 1)
        s.size = 7
        self.assertEqual(49, s.area())

    def test_area_one_arg(self):
        s = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            s.area(1)


class TestSquareStdout(unittest.TestCase):
    """Tests __str__ and display methods of Square class."""

    @staticmethod
    def capture_stdout(sq, method):
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return capture

    def test_str_method_print_size(self):
        s = Square(4)
        capture = self.capture_stdout(s, "print")
        self.assertEqual("[Square] ({}) 0/0 - 4\n".format(s.id), capture.getvalue())

    def test_str_method_size_x(self):
        s = Square(5, 5)
        self.assertEqual("[Square] ({}) 5/0 - 5".format(s.id), s.__str__())

    def test_str_method_size_x_y(self):
        s = Square(7, 4, 22)
        self.assertEqual("[Square] ({}) 4/22 - 7".format(s.id), str(s))

    def test_str_method_size_x_y_id(self):
        s = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(s))

    def test_str_method_changed_attributes(self):
        s = Square(7, 0, 0, [4])
        s.size = 15
        s.x = 8
        s.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", s.__str__())

    def test_display_method_size(self):
        s = Square(2)
        capture = self.capture_stdout(s, "display")
        expected_output = "##\n##\n"
        self.assertEqual(expected_output, capture.getvalue())

    def test_display_method_size_x(self):
        s = Square(3, 3)
        capture = self.capture_stdout(s, "display")
        expected_output = "   ###\n   ###\n   ###\n"
        self.assertEqual(expected_output, capture.getvalue())

    def test_display_method_size_x_y(self):
        s = Square(2, 1, 2)
        capture = self.capture_stdout(s, "display")
        expected_output = "\n\n #\n #\n"
        self.assertEqual(expected_output, capture.getvalue())

    def test_display_method_size_x_y_id(self):
        s = Square(2, 1, 2, 9)
        capture = self.capture_stdout(s, "display")
        expected_output = "\n\n #\n #\n"
        self.assertEqual(expected_output, capture.getvalue())


if __name__ == '__main__':
    unittest.main()
