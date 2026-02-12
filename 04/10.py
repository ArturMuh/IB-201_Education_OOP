class Triangle:
    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        self.sides = (a,b,c)

    def Perimeter(self) -> int:
        return sum(self.sides)

class EquilateralTriangle(Triangle):
    def __init__(self, side: int) -> None:
        self.sides = (side, side, side)