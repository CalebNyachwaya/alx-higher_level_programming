#!/usr/bin/python3
"""import json module"""
import json


def load_from_json_file(filename):
    """
    Reads a JSON file and converts it into a Python object.

    Args:
        filename (str): The name of the JSON file to be read.
    """
    with open(filename, 'r') as file:
        return json.load(file)
