#!/usr/bin/python3

class Square:
    """
    This class defines a square
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with '#' characters.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
