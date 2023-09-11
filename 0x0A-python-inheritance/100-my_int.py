#!/usr/bin/python3
"""
This module contains the MyInt class that inherits from int
with inverted == and != operators.
"""


class MyInt(int):
    """
    A class representing MyInt, which is a rebel with inverted
    == and != operators.
    """

    def __eq__(self, other):
        """
        Overrides the == operator to return the inverted result.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator to return the inverted result.
        """
        return super().__eq__(other)
