#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """
    This class defines a square by specifying the size.
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
