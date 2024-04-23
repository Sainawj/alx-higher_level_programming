#!/usr/bin/python3
"""
Defines a base model class.
"""
import json
import csv
import turtle


import json
import csv
import turtle


class Base:
    """Base model class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize instance with an id."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON string representation of list_objs to file."""
        file_name = f"{cls.__name__}.json"
        with open(file_name, "w") as jsonfile:
            if not list_objs:
                jsonfile.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Return list from JSON string."""
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create instance with attributes set from dictionary."""
        dummy = cls(1) if cls.__name__ == "Rectangle" else cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load instances from JSON file."""
        file_name = f"{cls.__name__}.json"
        try:
            with open(file_name, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write CSV serialization of list_objs to file."""
        file_name = f"{cls.__name__}.csv"
        with open(file_name, "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls._fields())
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Load instances from CSV file."""
        file_name = f"{cls.__name__}.csv"
        try:
            with open(file_name, "r") as csvfile:
                reader = csv.DictReader(csvfile)
                return [cls.create(**row) for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using turtle."""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#3399FF")
        turt.pensize(4)
        turt.shape("turtle")

        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#FFFF00")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()

    @classmethod
    def _fields(cls):
        """Return fields used in CSV serialization."""
        if cls.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        else:
            return ["id", "size", "x", "y"]
