class Temperature:

    @staticmethod
    def c_to_f(c: float) -> float:
        f = c * 9 / 5 + 32
        return round(f, 2)

    @staticmethod
    def f_to_c(f: float) -> float:
        c = (f - 32) * 5 / 9
        return round(c, 2)

print(Temperature.c_to_f(0))
print(Temperature.f_to_c(212))
print(Temperature.c_to_f(-40))
print(Temperature.f_to_c(-40))
