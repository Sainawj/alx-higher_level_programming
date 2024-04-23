#!/usr/bin/python3

"""Unit tests for Base class instantiation."""


import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    """Tests for the instantiation of the Base class."""

    def test_no_argument(self):
        """Test instantiation with no arguments."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        """Test instantiation of three Base instances."""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        """Test instantiation with None as id."""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        """Test instantiation with a unique id."""
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        """Test number of instances after instantiation with a unique id."""
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        """Test if id attribute is public."""
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        """Test if __nb_instances attribute is private."""
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_invalid_id_types(self):
        """Test instantiation with invalid id types."""
        invalid_ids = [
            "hello",
            5.5,
            complex(5),
            {"a": 1, "b": 2},
            True,
            [1, 2, 3],
            (1, 2),
            {1, 2, 3},
            frozenset({1, 2, 3}),
            range(5),
            b'Python',
            bytearray(b'abcefg'),
            memoryview(b'abcefg'),
            float('inf'),
            float('nan')
        ]
        for invalid_id in invalid_ids:
            with self.subTest(invalid_id=invalid_id):
                self.assertRaises(TypeError, Base, invalid_id)

    def test_two_args(self):
        """Test instantiation with more than one argument."""
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()
