class BoundingRectangle:
    def __init__(self):
        self.x = []
        self.y = []

    def add_point(self, x, y):
        self.x.append(x)
        self.y.append(y)

    def width(self):
        return max(self.x) - min(self.x)

    def height(self):
        return max(self.y) - min(self.y)

    def bottom_y(self):
        return min(self.y)

    def top_y(self):
        return max(self.y)

    def left_x(self):
        return min(self.x)

    def right_x(self):
        return max(self.x)


rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())

rect = BoundingRectangle()
rect.add_point(10, 20)
rect.add_point(5, 7)
rect.add_point(6, 3)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())


rect = BoundingRectangle()
rect.add_point(-11, -12)
rect.add_point(13, -14)
rect.add_point(-15, 10)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print()
rect.add_point(-21, -12)
rect.add_point(13, -14)
rect.add_point(-15, 36)
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print()
rect.add_point(-21, 78)
rect.add_point(13, -14)
rect.add_point(-55, 36)
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
print(rect.left_x(), rect.right_x())