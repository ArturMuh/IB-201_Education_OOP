class Profile:
    def __init__(self, profession: str) -> None:
        self.profession = profession

    def info(self) -> str:
        return ''

    def describe(self) -> None:
        print(f"{self.profession}{self.info()}")

class Vacancy(Profile):
    def __init__(self, profession: str, salary: int | float) -> None:
        self.profession = profession
        self.salary = salary

    def info(self) -> str:
        return f'Предлагаемая зарплата: {self.salary}'

class Resume(Profile):
    def __init__(self, profession: str, experience: int | float) -> None:
        self.profession = profession
        self.experience = experience

    def info(self) -> str:
        return f'Стаж работы: {self.experience}'


