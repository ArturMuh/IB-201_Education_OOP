# class Password:
#
#     @staticmethod
#     def is_strong(p: str) -> bool:
#         if len(p) < 8:
#             return False
#         has_digit = any(char.isdigit() for char in p)

class Password:
    MIN_LENGTH = 8

    @staticmethod
    def is_strong(p: str) -> bool:
        if len(p) < Password.MIN_LENGTH:
            return False

        has_digit = False
        for char in p:
            if char.isdigit():
                has_digit = True
                break

        if not has_digit:
            return False

        has_upper = False
        for char in p:
            if char.isupper():
                has_upper = True
                break

        if not has_upper:
            return False

        has_lower = False
        for char in p:
            if char.islower():
                has_lower = True
                break

        return has_lower

print(Password.is_strong('qwerty'))
print(Password.is_strong('Qwerty12'))
print(Password.is_strong('QWERTY12'))
print(Password.is_strong('Qwerty123'))