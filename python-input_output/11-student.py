#!/usr/bin/python3
"""Module that defines Student class with serialization"""


class Student:
    """A class that defines a student with serialization support"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student

        Args:
            first_name: the first name of the student
            last_name: the last name of the student
            age: the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance

        Args:
            attrs: list of attribute names to retrieve or None for all

        Returns:
            dictionary representation of the Student
        """
        if isinstance(attrs, list):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json: dictionary containing attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
