class BankAccount:
    def __init__(self, initial: int) -> None:
        self.__balance = initial

    @property
    def balance(self) -> int:
        return self.__balance # только доя чтения

    def deposit(self, amount: int) -> None:
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount: int) -> bool:
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            return True
        return False

acc = BankAccount(100)

print(acc.balance)
acc.deposit(50)
print(acc.balance)

print(acc.withdraw(30))
print(acc.balance)

print(acc.withdraw(1000))
print(acc.balance)
