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
        __position (tuple): Tuple of 2 positive integer.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square with the given size.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple):  tuple of 2 positive integers
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2 and
                isinstance(value[0], int) and isinstance(value[1], int) and
                (value[0] > 0 and value[1] > 0)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Public instance method: def my_print(self):
            that prints in stdout the square with the character #:
            if size is equal to 0, print an empty line"""
        if self. __size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print("")

        for num in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
