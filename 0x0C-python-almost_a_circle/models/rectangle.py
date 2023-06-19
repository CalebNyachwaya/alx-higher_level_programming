#!/usr/bin/python3
# rectangle.py
""" module imports module base """
from models.base import Base


class Rectangle(Base):
    """ inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        super().__init__(id)

    @property
    """Getter method for width attribute"""
    def width(self):
        return self.__width

    @width.setter
    """Setter method for width attribute"""
    def width(self, value):
        self.__width = value

    @property
    """Setter method for height attribute"""
    def height(self):
        return self.__height

    @height.setter
    """Setter method for height attribute"""
    def height(self, value):
        self.__height = value

    @property
    """Getter method for x attribute"""
    def x(self):
        self.__x = x

    @x.setter
    """Setter method for x attribute"""
    def x(self, value):
        self.__x = value

    @property
    """Getter method for y attribute"""
    def y(self):
        return self.__y

    @y.setter
    """Setter method for y attribute"""
    def y(self, value):
        self.__y = value
