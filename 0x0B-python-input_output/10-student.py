#!/usr/bin/python3
"""Defines students class"""


class Student:
    """Defines student data here"""
    def __init__(self, first_name, last_name, age):
        """Creates new instances of Student.

        Args:
            first_name (str): first name of student.
            last_name (int): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a dictionary representation of a Student instance.

        Returns:
            dict: dictionary representation
        """
        if attrs = None:
            return self.__dict__
        
        new_dict = {}
        for item in attr:
            try:
                new_dict[item] = self.__dict__
            except Exception:
                pass
        return new_dict
