class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y # если точки координат равны

    def __ne__(self, other) -> bool:

        return not (self == other) # если точки коодинат не равны

p1 = Point(1, 2)
p2 = Point(5, 6)

if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

if p1 != p2:
    print("Not equal True")
else:
    print("Not equal False")

p1 = Point(0, 0)
p2 = Point(0, 0)

if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

if p1 != p2:
    print("Not equal True")
else:
    print("Not equal False")

p1 = Point(0, 10)
p2 = Point(0, 0)

if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

if p1 != p2:
    print("Not equal True")
else:
    print("Not equal False")