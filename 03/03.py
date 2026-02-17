class SquareFunction:
    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, x: int) -> int | float:
        return self.a * x ** 2 + self.b * x + self.c

sf = SquareFunction(1, 0, 0)
print(sf(-2))
print(sf(-1))
print(sf(-0))
print(sf(1))
print(sf(2))
print(sf(10))
