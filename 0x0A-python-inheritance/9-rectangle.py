#!/usr/bin/python3

"""Module of class Rectangle that inherits from BaseGeometry"""

# Import BaseGeometry class from module 7-base_geometry
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Constructor for Rectangle class that initializes private attributes.

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """

    def __init__(self, width, height):
        """
        Initialize the Rectangle object with width and height.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        # Call integer_validator to validate width and height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        # Initialize private attributes __width and __height
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: the calculated area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Get a string representation of the rectangle.

        Returns:
            str: string representation of the rectangle
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
