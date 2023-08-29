#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """
    This class defines a square
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return (self.__size ** 2)
