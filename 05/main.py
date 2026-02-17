# Режимы доступа public, private, protected. Сеттеры и геттеры
# class Circle:
#     def __init__(self, radius: int | float) -> None:
#         self._radius = radius
#
#     def test_m(self):
#         self._radius = 15
#
#     def __str__(self):
#         return f'Radius: {self._radius}'
#
# c = Circle(radius=5)
# print(c)  # Radius: 5
# c.radius = 10  # Создает новый атрибут
# print(c)
# # c.test_m()
# # print(c)

class Rectangle:
    def ＿init＿(self, widht: int | float, height: int | float) -> None:
        self.＿width = widht
        self. ＿height = height
    def ＿str＿(self) -> str:
        return f'W: {self. ＿width}, H: {self. ＿height}'
class Square(Rectangle):
    def ＿init＿(self, side: int | float) -> None:
        self.＿width = side
        self. ＿height = side

s = Square(10)
s._width = 20
print(s)