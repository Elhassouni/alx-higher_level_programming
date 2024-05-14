#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module provides the Square class, which allows for the creation
of square objects with a given size, and includes methods to
get the size and calculate the area of the square."""


class Square:
    """Represents a square with a specific size.

    Attributes:
        __size (int): The size of one side of the square.
    """

    def __init__(self, size=0):
        """Initializes a new square with the given size.

        Args:
            size (int): The size of the square. Defaults to 0.
        """
        self.__size = size

    @property
    def size(self):
        """int: Gets or sets the size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than or equal to 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
