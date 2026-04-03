# прототип
# прототип порождающий паттернт

# class CustomObject(): # праметр прототипа
#     def __init__(self, param: str) -> None:
#         self.param = param
#
# a = CustomObject('А')
# b = a
# print(id(a), id(b))
from datetime import datetime as dt

# class CustomObject(): # праметр прототипа
#     def __init__(self, param: str) -> None:
#         self.param = param
#         self.date = dt.now()
#         self.__test = dt.now()
#
#     @property
#     def test(self):
#         return self.__test
#
# def clon(obj: CustomObject) -> CustomObject: # клонирование даты и время. функция clon независимая
#     new_obj = CustomObject(obj.param)
#     new_obj.date = obj.date
#     return new_obj
#
# a = CustomObject('А')
# b = clon(a)
# print('A:',id(a),a.param, a.date, a.test)
# print('B:', id(b), b.param, b.date, b.test) # простой метод клонирования

# структура

# from abc import abstractmethod
# from datetime import datetime as dt
#
# class IPrototype:
#     @abstractmethod
#     def clon(self):
#         pass
#
# class Table(IPrototype):
#     name: str | None = None
#     color: str | None = None
#
#     def __init__(self, name: str, color: str = None) -> None:
#         self.name = name
#         self.color = color
#
#     def update_name(self) -> None:
#         self.name += ' ' + str(dt.now())
#
#     def clon(self):
#         obj = Table(name=self.name)
#         obj.color = self.color
#         return obj
#
#     def __repr__(self) -> str:
#         return self.name + ' ' + str(self.color)
#
# a = Table('Прикроватный')
# a.update_name()
# print(id(a), ":",a)
# b = a.clon()
# b.update_name()
# print(id(b), ":",b)

# Псевдокод

from abc import abstractmethod
from datetime import datetime as dt

class IShape:
    @abstractmethod
    def clon(self):
        pass


class Circle(IShape):
    def __init__(self, radius: int | float) -> None:
        self.__radius = radius # мы можем написать приватные переменные

    def clon(self):
        return Circle(radius=self.__radius)

    def __repr__(self) -> str:
        return f'Circle({self.__radius})'

class Rectangle(IShape):
    def __init__(self, width: int | float, height: int | float) -> None:
        self.__width = width # мы можем написать приватные переменные
        self.__height = height

    def clon(self):
        return Rectangle(width=self.__width, height=self.__height)

    def __repr__(self) -> str:
        return f'Rectangle({self.__width}, {self.__height})'

c = Circle(4)
print(c)
c2 = c.clon()
print(c2)

r = Rectangle(10,15)
print(r)
r2 = r.clon()
print(r2)







