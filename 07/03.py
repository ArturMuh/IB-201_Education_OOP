class User:
    id_counter = 0

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name

    @classmethod
    def create(cls, name: str) -> "User":
        cls.id_counter += 1
        return cls(cls.id_counter, name)

    @classmethod
    def count(cls) -> int:
        return cls.id_counter

u1 = User.create("Ann")
u2 = User.create("Bob")
u3 = User.create("Cory")
print(u1.id, u2.id, u3.id)
print(User.count())
