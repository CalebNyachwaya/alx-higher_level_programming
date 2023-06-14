#!/usr/bin/python3
"""import module json"""
import json


def to_json_string(my_obj):
    """
    Convert an object to its JSON representation as a string.
    Args:
        my_obj (object): The object to be converted to JSON.
    """
    json_string = json.dumps(my_obj)
    return json_string
