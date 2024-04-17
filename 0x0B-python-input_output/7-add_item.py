#!/usr/bin/python3
"""script that adds all arguments to a Python list then save them to a file"""


import json
import os.path
import sys


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to write to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)


def load_from_json_file(filename):
    """Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)


filename = "add_item.json"
json_list = []


if os.path.exists(filename):
    json_list = load_from_json_file(filename)

for index in sys.argv[1:]:
    json_list.append(index)

save_to_json_file(json_list, filename)
