class User:
    def solve(self, n:int):
        pass

class Student(User):
    pass

class Teacher(User):
    def check_solution(self, user: User, n:int) -> None:
        pass

class Admin(User):
    def edit(self, n: int) -> None:
        pass

class SuperAdmin(Admin):
    def grant(self, user: User) -> None:
        pass


