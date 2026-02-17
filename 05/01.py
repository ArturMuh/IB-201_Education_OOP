class User:
    def __init__(self, username: str, password: int) -> None:
        self.username1 = username
        self.passwords = password

    @property
    def username(self) -> str: # доступен только для чтения
        return self.username1

    def check_password(self, password: bool) -> bool:
        return self.passwords == password

    def set_password(self, old_password: str, new_password: str) -> bool:
        if self.passwords == old_password:
            self.passwords = new_password
            return True
        return False

u = User("alice", "1234")

print(u.username)
print(u.check_password("0000"))
print(u.check_password("1234"))

print(u.set_password("0000", "abcd"))
print(u.set_password("1234", "abcd"))
print(u.check_password("abcd"))

