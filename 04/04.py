class User:
    def __init__(self, name: str) -> None:
        self.name = name

    def send_message(self,user, message):
        pass

    def post(self, message):
        pass

    def info(self) -> str:
        return ''

    def describe(self) -> str:
        print(f"{self.name}{self.info()}")

class Person(User):
    def __init__(self,name:str, birthdate:str) -> None:
        self.name = name
        self.birthdate = birthdate

    def info(self) -> str:
        return f" Дата рождения: {self.birthdate}"

    def subscribe(self, user: User) -> None:
        pass

class Community(User):
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    def info(self) -> str:
        return f" Описание: {self.description}"

# Почему то предупреждение указывается на метод __init__







