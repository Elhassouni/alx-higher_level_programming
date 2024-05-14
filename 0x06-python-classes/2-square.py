#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Square Class

This is an empty square class
Author: Ayoub

"""

""" This is a Module """


class Square:
    """ This is an Empty class """
    def __init__(self, size=0):
        """ check if the size is an integer """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        """check size """
        if size < 0:
            raise ValueError("size must be >= 0")
        """The type check and value check should be done before assigning the
            value to the attribute."""
        self.__size = size
