class Counter:
    def __init__(self, start: int = 0):
       self._value = start

    def inc(self) -> int:
        self._value += 1
    def dec(self) -> int:
        self._value -= 1
    def value(self) -> int:
        return self._value


# class LimitedCounter(Counter):
#     def __init__(self, min_value: int = 0, max_value: int = 100, start: int = 0) -> None:
#         super().__init__(start)
#         self.min_value = min_value
#         self.max_value = max_value
#
#         if self._value < self.min_value:
#             self._value = self.min_value
#         elif self._value > self.max_value:
#             self._value = self.max_value
