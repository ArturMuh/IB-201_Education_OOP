# Поведенческий паттерн
# цепочка обязанностей
from abc import abstractmethod
from datetime import datetime as dt


class IHandler: # эта цепочка обработчиков, каждый из которых либо
# обрабатывает запрос, либо передает дальше по цепочке.
    @abstractmethod
    def set_next(self, handler: 'IHandler') -> None: # установливает обработчик запроса
        pass

    @abstractmethod
    def handle(self, request: str) -> str | None: # здесь он обрабатывет цепочку или передает дальше
        pass


class BaseHandler(IHandler):
    next_handler: IHandler | None = None

    def set_next(self, handler: IHandler) -> IHandler: # он запоминает, кто следующий
        # в цепочке, и возвращает его
        self.next_handler = handler
        return handler

    def handle(self, request: str) -> str | None: # Если есть следующий обработчик - передает ему или ничего не возв.
        if self.next_handler:
            return self.next_handler.handle(request)
        return None


class ConcreteHandlers(BaseHandler): # этот класс проверяет может ли запрос обработать если да то делает и возвращает
    @abstractmethod
    def can_handle(self, request: str) -> bool:
        pass

    def handle(self, request: str) -> str | None:
        if self.can_handle(request):
            return f'ConcreteHandlers обработал: {request}'
        else:
            print(f'ConcreteHandlers передаёт дальше: {request}') # если нет то передает дальше
            return self.next_handler.handle(request) if self.next_handler else None


class HandlerA(ConcreteHandlers):
    def can_handle(self, request: str) -> bool: # обработчик берет А и передает дальше и т.д
        return request == 'A'

    def handle(self, request: str) -> str | None:
        if self.can_handle(request):
            return f'HandlerA обработал: {request}'
        else:
            print(f'HandlerA передаёт дальше: {request}')
            return self.next_handler.handle(request) if self.next_handler else None


class HandlerB(ConcreteHandlers):
    def can_handle(self, request: str) -> bool:
        return request == 'B'

    def handle(self, request: str) -> str | None:
        if self.can_handle(request):
            return f'HandlerB обработал: {request}'
        else:
            print(f'HandlerB передаёт дальше: {request}')
            return self.next_handler.handle(request) if self.next_handler else None


class HandlerC(ConcreteHandlers):
    def can_handle(self, request: str) -> bool:
        return request == 'C'

    def handle(self, request: str) -> str | None:
        if self.can_handle(request):
            return f'HandlerC обработал: {request}'
        else:
            print(f'HandlerC передаёт дальше: {request}')
            return self.next_handler.handle(request) if self.next_handler else None



h1 = HandlerA()
h2 = HandlerB()
h3 = HandlerC()

h1.set_next(h2).set_next(h3)

print(h1.handle("A"))
print(h1.handle("B"))
print(h1.handle("C"))
print(h1.handle("D"))


