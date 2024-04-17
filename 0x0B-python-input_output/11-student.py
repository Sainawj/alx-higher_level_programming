#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Class to represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): List of strings containing attribute names.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            return {attr: getattr(self, attr) for attr in attrs}

    def reload_from_json(self, json_data):
        """Reload a Student instance from a dictionary representation.

        Args:
            json_data (dict): Dictionary containing student information.

        Returns:
            None
        """
        for key, value in json_data.items():
            setattr(self, key, value)
