#!/usr/bin/python3
"""
This module defines a function save_to_json_file that writes an object to a text file
using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be saved to the file.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
