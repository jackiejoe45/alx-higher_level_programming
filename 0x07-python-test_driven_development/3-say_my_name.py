#!/usr/bin/python3
"""

This modules defines the say_my_name function

"""
def say_my_name(first_name, last_name=""):
    """
    This function displays the name(s) provded as arguments in a sentence

    Args:
        first_name: The first argument
        last_name: The last argument
    Raises:
        TypeError: first_name is not a string
        TypeError: last_name is not a string
    """
    if not isinstance(first_name,str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name,str):
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
