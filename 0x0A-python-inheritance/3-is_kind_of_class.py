#!/usr/bin/python3
"""
This module contains the is_kind_of_class function.
"""

def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if it's an instance of a class that inherited from,
    the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
