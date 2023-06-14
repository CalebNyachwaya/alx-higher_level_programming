#!/usr/bin/python3
"""
A module that provides a function to convert a dictionary
representation of a class object to a JSON-like data structure.
"""


def class_to_json(obj):
    """Converts a class object to a JSON-like data structure.

    Args:
        obj (dict): Instance of a class.

    Returns:
        dict: Dictionary representation of the class object.
    """
    return obj.__dict__
