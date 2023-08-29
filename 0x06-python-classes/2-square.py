import math
"""A module that defines a square """


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

    @property
    def radius(self):
        """
        Retrieves the value of the radius attribute.
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Sets the value of the radius attribute with type and value checks.
        """
        if not isinstance(value, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = value

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
