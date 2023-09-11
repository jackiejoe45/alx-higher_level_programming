#!/usr/bin/python3
"""
This module contains the lookup function.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to look up.

    Returns:
        A list of strings representing the attributes and methods ofan object.
    """
    return dir(obj)
