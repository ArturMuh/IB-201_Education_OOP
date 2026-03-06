def check_password(func):

    def wrapper(*args, **kwargs):
        password = input("Введите пароль: ")

        if password == "Artur":
            print("Доступ разрешен")
            return func(*args, **kwargs)

        else:
            print("В доступе отказано")
            return None # он здесь возвращает если пароль не верный

    return wrapper

@check_password
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


fib(15)