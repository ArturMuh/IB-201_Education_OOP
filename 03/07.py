class Polynomial:
    def __init__(self, coefficients: list[int]):
        self.coefficients = coefficients

    def __call__(self, x: int | float) -> int | float:
        result = 0
        for power, coeff in enumerate(self.coefficients):
            result += coeff * (x ** power)
        return result

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))  # Находим максимальную степень
        coeffs1 = self.coefficients + [0] * (max_len - len(self.coefficients))
        coeffs2 = other.coefficients + [0] * (max_len - len(other.coefficients))
        result_coeffs = []
        for i in range(max_len):
            result_coeffs.append(coeffs1[i] + coeffs2[i])
        while len(result_coeffs) > 1 and result_coeffs[-1] == 0:
            result_coeffs.pop()

        return Polynomial(result_coeffs)

    def __repr__(self):
        return f"Polynomial({self.coefficients})"

poly = Polynomial([10, -1])
print(poly(0))  # 10 - 0 = 10
print(poly(1))
print(poly(2))

poly1 = Polynomial([0, 0, 1])
print(poly1(-2))
print(poly1(-1))
print(poly1(0))
print(poly1(1))
print(poly1(2))
print()

poly2 = Polynomial([0, 0, 2])
print(poly2(-2))
print(poly2(-1))
print(poly2(0))
print(poly2(1))
print(poly2(2))
print()

poly3 = poly1 + poly2
print(poly3(-2))
print(poly3(-1))
print(poly3(0))
print(poly3(1))
print(poly3(2))
print()

poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1

print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))



