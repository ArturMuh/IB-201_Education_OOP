class BaseObject:
    def __init__(self, x: int | float,y: int | float, z: int | float) -> None:
        self.x = x # это баззовый класс с координатами
        self.y = y
        self.z = z

    def get_coordinates(self):
        return self.x, self.y, self.z

class Block(BaseObject):
    def shatter(self) -> None:
        self.x = None
        self.y = None
        self.z = None

class Entity(BaseObject):
    def move(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


class Thing(BaseObject):
    pass #это предмет объекта координат



