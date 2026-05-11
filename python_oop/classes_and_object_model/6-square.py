#!/usr/bin/env python3
"""Module that defines a Square class."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with optional size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position: must be a tuple of 2 non-negative integers."""
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square as a string using # and spaces for position."""
        if self.__size == 0:
            return ""
        lines = [""] * self.__position[1]
        row = " " * self.__position[0] + "#" * self.__size
        lines += [row] * self.__size
        return "\n".join(lines)

    def my_print(self):
        """Print the square with # characters using position as offset."""
        print(self)
