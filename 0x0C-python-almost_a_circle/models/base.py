#!/usr/bin/python3
"""
Defines a base model class.
"""


import json
import csv
import turtle


class Base:
    """
    Represents the base model
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        file_name = f"{cls.__name__}.json"
        with open(file_name, "w") as jsonfile:
            list_dict = [obj.to_dictionary() for obj in list_objs] if list_objs else []
            jsonfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Parses a JSON string and returns the corresponding list of dictionaries."""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        instance = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """Loads instances from a JSON file."""
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV serialization of a list of objects to a file."""
        file_name = f"{cls.__name__}.csv"
        with open(file_name, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.fields())
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads instances from a CSV file."""
        file_name = f"{cls.__name__}.csv"
        try:
            with open(file_name, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                return [cls.create(**row) for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def fields():
        """Returns the field names for CSV serialization."""
        return ["id", "width", "height", "x", "y"]

    @staticmethod
    def draw(list_shapes):
        """Draws shapes using the turtle module."""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#3399FF")
        turt.pensize(4)
        turt.shape("turtle")

        for shape in list_shapes:
            turt.showturtle()
            turt.up()
            turt.goto(shape.x, shape.y)
            turt.down()
            for _ in range(2):
                turt.forward(shape.width)
                turt.left(90)
                turt.forward(shape.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
