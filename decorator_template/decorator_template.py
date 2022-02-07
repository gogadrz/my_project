def decorator(func):
    def wrapped_func(*args, **kwargs):
        # Код до вызова функции
        value = func(*args, **kwargs)
        # Код после вызова функции
        return value
    return wrapped_func


@decorator
def some_function(*args):
    pass
