#!/usr/bin/python3
"""
This module contains the is_kind_of_class function.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if object is an instance of, or instance of a class that
    inherited from,the specified class.
    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance or subclass of a_class, else False.
    """
    return isinstance(obj, a_class)
