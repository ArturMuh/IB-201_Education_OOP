from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self, text: str) -> None: ...


class Scannable(ABC):
    @abstractmethod
    def scan(self) -> str: ...


class Faxable(ABC):
    @abstractmethod
    def fax(self, number: str) -> None: ...


class Copiable(ABC):
    @abstractmethod
    def copy(self) -> None: ...


class SimplePrinter(Printable):
    def print(self, text: str) -> None:
        print(text)