#!/usr/bin/python3
"""A module that defines a square """


class Square:
    """
    This class defines a square
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a specified size.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the value of the size attribute.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of the size attribute with type and value checks.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares two Square instances for equality based on area.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares the area of the square to the area of another
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compares the area of the square to the area of another
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares the area of the square to the area of another
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compares the area of the square to the area of another
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares the area of the square to the area of another.
        """
        return self.area() <= other.area()
