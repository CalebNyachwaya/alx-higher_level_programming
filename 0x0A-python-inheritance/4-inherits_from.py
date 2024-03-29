#!/usr/bin/python3
"""
function that returns True if the object is an instance of
a class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """ Function checks if the obj is the same type """

    if not type(obj) == a_class:
        if isinstance(obj, a_class):
            return True
        else:
            return False
    return False
