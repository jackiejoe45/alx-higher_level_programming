#!/usr/bin/python3
"""
This module defines a function class_to_json that returns a dictionary description
with simple data structures (list, dictionary, string, integer, and boolean) for JSON serialization
of an object.
"""

def class_to_json(obj):
    """
    Returns a dictionary description with simple data structures for JSON serialization of an object.

    Args:
        obj: The object to be converted to a JSON-serializable dictionary.

    Returns:
        dict: A dictionary representation of the object.
    """
    # Create an empty dictionary to store the serialized attributes
    serialized = {}

    # Iterate through the attributes of the object
    for attr, value in obj.__dict__.items():
        # Check if the value is of a serializable type (list, dict, str, int, bool)
        if isinstance(value, (list, dict, str, int, bool)):
            # Add the attribute and its value to the dictionary
            serialized[attr] = value

    return serialized
