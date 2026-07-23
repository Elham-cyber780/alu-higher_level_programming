#!/usr/bin/python3
"""Module that defines Student class"""


class Student:
    """A class that defines a student"""

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

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance

        Returns:
            dictionary representation of the Student
        """
        return self.__dict__
