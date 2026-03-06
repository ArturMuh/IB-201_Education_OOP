# Переопределение функций и декораторы

# def main_answer():
#     return 42
# Декотором называется функция которая принимает функцию и возвращает функцию
# input main_answer()
# x = input()
# print(x)

# def log(*args, **kwargs):
#     pass
#
# log("Enter to the system")
# log(2025,10,12, 'Enter')

# декораторы, логирование функции
# декораторы не должны портить, изменять поведение функции не нтак сильно

# @logged

from datetime import datetime as dt
def logged(func):
    count = 0

    def decorated_func(*args, **kwargs):
        nonlocal count
        count += 1
        print(count, '>>', 'Arguments:', args, 'Named arguments:', kwargs)
        result = func(*args, **kwargs)
        print('--', 'Result:', result)
        return result

    return decorated_func


@logged
def make_burger(type_of_meat, with_onion=False, with_tomato=True):
    print('Булочка')
    if with_onion:
        print('Луковые колечки')
    if with_tomato:
        print('Ломтик помидора')
    print('Котлета из', type_of_meat)
    print('Булочка')


@logged
def drinking_type(type):
    return 'У нас есть только чай'

# связано с декораторами фунции письма с приглащениями на какой-то адрес например число, город, текст, сообщение, имя но будет меняться все эти данные бот, email


    @classmethod # это экзмпляр класса. данный метод может обращаться только к атрибутам текущего класса, но не к локальным свойствам его экземпляров.
    # cls – ссылка на класс, а не self ссылка на объекта атрибута
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

# @staticmethod это статический метод которые определаются декораторами которые не имеют доступа ни к атрибутам класса, ни к атрибутам его экземпляров, то есть, некая независимая, самостоятельная функция