#!/usr/bin/python3
"""
This module defines a function class_to_json
that returns a dictionary description
with simple data structures
(list, dictionary, string, integer, and boolean)
for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns a dictionary description with simple
    data structures for JSON serialization of an object.

    Args:
        obj: The object to be converted to a JSON-serializable dictionary.

    Returns:
        dict: A dictionary representation of the object.
    """
    serialized = {}

    for attr, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serialized[attr] = value

    return serialized
