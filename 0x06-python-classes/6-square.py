#!/usr/bin/python3

class Square:
    """
    This class defines a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with an optional size and position.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieves the value of the position attribute.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the value of the position attribute with type and value checks.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(val, int) and val >= 0 for val in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """
        Prints the square with '#' characters, considering the position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
