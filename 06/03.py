from datetime import datetime as dt

def check_password(required_password):

    def decorator(func):
        def wrapper(*args, **kwargs):
            enter_password = input("Пароль: ")
            if enter_password == required_password:
                print("Пароль верный. Доступ разрешен.")
                return func(*args, **kwargs)
            else:
                print("Неверный пароль. Доступ запрещен.")
                return None
        return wrapper
    return decorator


@check_password('Artur')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    print("Булочка")
    if withOnion:
        print("Луковые колечки")
    if withTomato:
        print("Ломтик помидора")
    print(f"Котлета из {typeOfMeat}")
    print("Булочка")
    return "Бургер готов!"


def drinking_type(type):
    return 'У нас есть только другой бургер'

make_burger('beef')
print('-' * 10)
burger = drinking_type('burger')
print(burger)



