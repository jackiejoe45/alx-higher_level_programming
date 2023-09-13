#!/usr/bin/python3
"""
This module defines a class Student that represents a student with first_name, last_name, and age attributes.
"""

class Student:
    """
    Represents a student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name, and age attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): A list of attribute names to retrieve. If None, retrieve all attributes.

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
