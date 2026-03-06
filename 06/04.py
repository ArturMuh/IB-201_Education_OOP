def cached(func):
    cache = {}
    def decorated_func(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache:
            print(f"Значение из кэша для аргументов {args}: {cache[key]}")
            return cache[key]
        print(f"Вычисляем значение для аргументов {args}")
        result = func(*args, **kwargs)

        cache[key] = result
        print(f"Сохранено в кэш: {result}")
        return result
    return decorated_func


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

fib(15)