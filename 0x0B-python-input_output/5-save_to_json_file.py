#!/usr/bin/python3
"""import json module"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file
    Args:
    my_obj - object to be converted to object and written to file
    filename - file
    """
    with open(filename, 'w', encoding="utf8") as f:
        json.dump(my_obj, f)
