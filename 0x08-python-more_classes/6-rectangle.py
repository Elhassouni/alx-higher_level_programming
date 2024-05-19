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
            with the character # and return resul """

        empty_str = ""
        if self.__width == 0 or self.__height == 0:
            return empty_str
        else:
            for times in range(self.__height):
                for i in range(self.__width):
                    empty_str += "#"
                empty_str += "\n"
            return empty_str.rstrip()

    def __repr__(self):
        """recreate new instance"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ decrement number of instances once an object instance deleted"""
        """ printing sting once instance delted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
