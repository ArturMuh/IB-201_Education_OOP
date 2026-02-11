class AmericanDate:
    def __init__(self, year: int, month: int, day: int):
        self.year = str(year)
        self.month = str(month)
        self.day = str(day)

    def set_year(self, year: int):
        self.year = str(year)

    def set_month(self, month: int):
        self.month = str(month)

    def set_day(self, day: int):
        self.day = str(day)

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        return f"{self.month.rjust(2, '0')}.{self.day.rjust(2, '0')}.{self.year}"

class EuropeanDate:
    def __init__(self, year: int, month: int, day: int):
        self.year = str(year)
        self.month = str(month)
        self.day = str(day)

    def set_year(self, year: int):
        self.year = str(year)

    def set_month(self, month: int):
        self.month = str(month)

    def set_day(self, day: int):
        self.day = str(day)

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        return f"{self.day.rjust(2, '0')}.{self.month.rjust(2, '0')}.{self.year}"

american = AmericanDate(2000, 4, 10)
european = EuropeanDate(2000, 4, 10)
print(american.format())
print(european.format())
