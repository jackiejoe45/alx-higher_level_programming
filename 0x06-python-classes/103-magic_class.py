#!/usr/bin/python3
import math
""" This is a Custom Magic Class"""

class MagicClass:
    """
    This class provides methods to perform calculations using a radius value.
    """
    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with an optional radius.
        """
        self.__radius = 0
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area using the radius attribute.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference using the radius attribute.
        """
        return 2 * math.pi * self.__radius
