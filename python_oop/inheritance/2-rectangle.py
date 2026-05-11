#!/usr/bin/env python3
"""Module that defines a Rectangle class inheriting from BaseGeometry."""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with area and string representation."""

    def __init__(self, width, height):
        """Initialize a Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a readable string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
