#!/usr/bin/python3
"""module based on 6-base_geometry.py"""


class BaseGeometry:
    """class based on previous file"""

    def area(self):
        """method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validate the value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherits from the BaseGeometry class"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
