#!/usr/bin/python3
"""
This module defines a function load_from_json_file that creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        object: The Python object created from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
