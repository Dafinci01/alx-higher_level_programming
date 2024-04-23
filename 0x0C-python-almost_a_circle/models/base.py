#!/usr/bin/python3
"""
Defines a base model class.
"""


class Base:
    """
    Represents the base model
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor
        Args:
            id (int) - id of each model
        Return:
            none
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
