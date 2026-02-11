# Полиморфизм

from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Square:
    def __init__(self, side):
        self.side = side


    def area(self):
        return self.side * self.side


    def perimeter(self):
        return 4 * self.side

    def print_shape_info(shape):
        print("Area = {}, perimeter = {}.".format(
            shape.area(), shape.perimeter()))

        square = Square(10)
        print_shape_info(square)  # Area = 100, perimeter = 40
        print_shape_info(circle)  # Area = 314.1592653589793, perimeter = 62.83185307179586.