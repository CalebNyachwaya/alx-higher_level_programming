#!/usr/bin/python3
# base.py
"""base module for project"""


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor """
        self.id = id
        if self.id:
            self.id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
