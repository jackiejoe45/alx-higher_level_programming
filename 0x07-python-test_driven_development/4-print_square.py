#!/usr/bin/python3
"""

This module define a function which prints squares

"""
def print_square(size):
    """
    This function prints a square of # with [size] x [size] dimensions

    Args:
        size: he size of the square

    Raises:
        TypeError:size is not an integer
        ValueError: size is less than or is zero
        TypeError: size is a float less than zero
    """
    if not isinstance(size,int):
        raise TypeError('size must be an integer')
    if size <= 0:
        raise ValueError('size must be > 0')
    if (size<0 & isinstance(size,float)):
        raise TypeError('size must be an integer')

    for i in range(size):
        print('#' * size)
