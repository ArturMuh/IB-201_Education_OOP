class Date:
    def __init__(self, month: int, day: int) -> None:
        self.month = month
        self.day = day # хранение

    def __sub__(self, other):
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Количество дней в каждом месяце
        def to_days(date):
            return sum(days[:date.month - 1]) + date.day  # складываем всех месяцев
        return to_days(self) - to_days(other)


jan5 = Date(1, 5)
jan1 = Date(1, 1)

print(jan5 - jan1) # на экране получаем 5 января - 1 января = 4
print(jan1 - jan5) # здесь -4
print(jan1 - jan1)
print(jan5 - jan5)

mar5 = Date(3, 1)
jan1 = Date(1, 1)

print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)
