# Наследование
 # Наследование это передача кода
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self) -> int|float:


        # def __str__(self) -> str: # Это метод возвращает строку
        #     return '456'
        # def __str(self) -> str:
        #     return '\n'.join([
        #         self.__class
        #     ])

        def __repr__(self) -> str:
            return '{}(S={}'

        # наследование от класса @abctracmethod
        # def get_area(self) -> int | float:
        # pass

        # инкапсуляция скрывает внутренние объекта класса а также снижает скорость доступа к данных
