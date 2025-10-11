"""
In this script, define a base class Shape
with a method area() and derived classes Rectangle and Circle,
each overriding the area() method to calculate their respective areas.
"""
import math

class Shape:

    def area(self):
        raise NotImplementedError()


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return  math.pi * self.radius * self.radius



