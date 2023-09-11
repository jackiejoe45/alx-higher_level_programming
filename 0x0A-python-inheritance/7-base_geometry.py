#!/usr/bin/python3
"""
This module contains the BaseGeometry class with the area and
integer_validator methods.
"""


class BaseGeometry:
    """
    A class representing BaseGeometry.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - If value is not an integer, raises a TypeError exception
        with the message '<name> must be an integer'.
        - If value is less than or equal to 0, raises a ValueError
        exception with the message '<name> must be greater than 0'.
        Args:
            name: A string representing the name of the value.
            value: The value to validate.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
