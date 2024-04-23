#!/usr/bin/python3

"""Defines unittests for models/rectangle.py."""


import unittest
from io import StringIO
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittests for the Rectangle class."""

    def test_area(self):
        r = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, r.area())

        r = Rectangle(999999999999999, 999999999999999999, 0, 0, 1)
        self.assertEqual(999999999999998999000000000000001, r.area())

        r = Rectangle(2, 10, 1, 1, 1)
        r.width = 7
        r.height = 14
        self.assertEqual(98, r.area())

        r = Rectangle(2, 10, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_str_and_display(self):
        r = Rectangle(4, 6)
        with StringIO() as captured_output:
            with redirect_stdout(captured_output):
                print(r)
            self.assertEqual("[Rectangle] (1) 0/0 - 4/6\n", captured_output.getvalue())

        r = Rectangle(5, 5, 1)
        self.assertEqual("[Rectangle] (2) 1/0 - 5/5", str(r))

        r = Rectangle(1, 8, 2, 4)
        self.assertEqual("[Rectangle] (3) 2/4 - 1/8", str(r))

        r = Rectangle(13, 21, 2, 4, 7)
        self.assertEqual("[Rectangle] (7) 2/4 - 13/21", str(r))

        r = Rectangle(7, 7, 0, 0, [4])
        r.width = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Rectangle] ([4]) 8/10 - 15/1", str(r))

        r = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

        r = Rectangle(2, 3, 0, 0, 0)
        with StringIO() as captured_output:
            with redirect_stdout(captured_output):
                r.display()
            self.assertEqual("##\n##\n##\n", captured_output.getvalue())

        r = Rectangle(3, 2, 1, 0, 1)
        with StringIO() as captured_output:
            with redirect_stdout(captured_output):
                r.display()
            self.assertEqual(" ###\n ###\n", captured_output.getvalue())

        r = Rectangle(4, 5, 0, 1, 0)
        with StringIO() as captured_output:
            with redirect_stdout(captured_output):
                r.display()
            self.assertEqual("\n####\n####\n####\n####\n####\n", captured_output.getvalue())

        r = Rectangle(2, 4, 3, 2, 0)
        with StringIO() as captured_output:
            with redirect_stdout(captured_output):
                r.display()
            self.assertEqual("\n\n   ##\n   ##\n   ##\n   ##\n", captured_output.getvalue())

        r = Rectangle(5, 1, 2, 4, 7)
        with self.assertRaises(TypeError):
            r.display(1)


if __name__ == "__main__":
    unittest.main()
