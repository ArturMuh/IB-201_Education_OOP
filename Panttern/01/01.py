from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Type


class Animal(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def make_sound(self) -> str:
        pass

    def get_info(self) -> str:
        return f"{self.name} издает звук: {self.make_sound()}"


class Lion(Animal):
    def __init__(self, name: str = "Лев"):
        super().__init__(name)

    def make_sound(self) -> str:
        return "Рычание!"


class Monkey(Animal):
    def __init__(self, name: str = "Обезьяна"):
        super().__init__(name)

    def make_sound(self) -> str:
        return "Визг!"


class Elephant(Animal):
    def __init__(self, name: str = "Слон"):
        super().__init__(name)

    def make_sound(self) -> str:
        return "Трубление!"

class Animal(ABC):
    @abstractmethod
    def make_sound(self) -> str:
        pass


class Lion(Animal):
    def make_sound(self) -> str:
        return "Рычание!"


class Monkey(Animal):
    def make_sound(self) -> str:
        return "Визг!"


class Elephant(Animal):
    def make_sound(self) -> str:
        return "Трубление!"

class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

    def interact_with_animal(self) -> None:
        animal = self.create_animal()
        print(f"Звук: {animal.make_sound()}")


class LionFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Lion()


class MonkeyFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Monkey()


class ElephantFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Elephant()

class AnimalType(Enum):
    LION = "lion"
    MONKEY = "monkey"
    ELEPHANT = "elephant"

class ZooFactory:
    _factories: Dict[AnimalType, Type[AnimalFactory]] = {
        AnimalType.LION: LionFactory,
        AnimalType.MONKEY: MonkeyFactory,
        AnimalType.ELEPHANT: ElephantFactory
    }

    @staticmethod
    def create_animal(animal_type: AnimalType, name: str = None) -> Animal:
        factory_class = ZooFactory._factories.get(animal_type)
        if factory_class:
            factory = factory_class()
            return factory.create_animal(name)
        raise ValueError(f"Неизвестный тип животного: {animal_type}")

def interact_with_animal(factory: AnimalFactory) -> None:
    animal = factory.create_animal()
    sound = animal.make_sound()
    print(f"Звук: {sound}")

lion_factory = LionFactory()
monkey_factory = MonkeyFactory()
elephant_factory = ElephantFactory()

interact_with_animal(lion_factory)     # Вывод: Звук: Рычание!
interact_with_animal(monkey_factory)   # Вывод: Звук: Визг!
interact_with_animal(elephant_factory) # Вывод: Звук: Трубление!