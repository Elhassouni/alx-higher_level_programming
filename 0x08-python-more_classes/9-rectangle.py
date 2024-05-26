#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" Rectangle

Class Rectangle that defines a rectangle by
Author: Ayoub

"""
""" This is a Module """


class Rectangle:
    """class Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter and setter to be validated and set as private
            Raise:
                TypeError: if the width is not an integer.
                ValueError: if the int is less then 0."""
        return self.__width

    @property
    def height(self):
        """ setting private attribute using property
            and chekching for type and value Error"""
        return self.__height

    @width.setter
    def width(self, value):
        """
            A property setter of height

            Args:
                value (int): the new width value to set

            Raises:
                TypeError: if width is not an int
                ValueError: if width < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ Returns the rectangle area"""
        result = self.__height * self.__width
        return result

    def perimeter(self):
        """ returns the rectangle perimeter"""

        result_perimeter = 0
        if self.__height == 0 or self.__width == 0:
            return result_perimeter
        else:
            result_perimeter = 2 * (self.__height + self.__width)
            return result_perimeter

    def __str__(self):
        """print() and str() should print the rectangle
        with the character stored in print_symbol and return result"""
        if self.__width == 0 or self.__height == 0:
            return ""

        symbol = str(self.print_symbol)
        """ Ensuring print_symbol is treated
            as a string"""
        rect_str = (symbol * self.__width + "\n") * self.__height
        return rect_str.rstrip()  # Remove the trailing newline

    def __repr__(self):
        """recreate new instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ decrement number of instances once an object instance deleted"""
        """ printing sting once instance delted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two Rectangle instances and returns the one with
            the greater or equal area.

        Parameters
        ----------
        rect_1 : Rectangle
            The first rectangle to compare.
        rect_2 : Rectangle
            The second rectangle to compare.

        Returns
        -------
        Rectangle
            The rectangle with the greater or equal area.
            If both areas are equal, rect_1 is returned.

        Raises
        ------
        TypeError
            If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Factory method to create a cube with equal width,
        height, and depth"""

        return cls(size, size)
