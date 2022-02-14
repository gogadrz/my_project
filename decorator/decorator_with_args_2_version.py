# модернизированная версия, если без аргумента, можно не писать скобки
# необязательный аргумент _func (return тоже другой)
# звездочка указывает, что все остальные аргументы передаются искльчительно по ключу
def timer_with_precision(_func: Optional[Callable] = None, *, precision: int = 1) -> Callable:
    def timer_decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped_func(*args, **kwargs) -> Any:
            # some code
            value = func(*args, **kwargs)
            # other code
            return value

        return wrapped_func

    if _func is None:
        return timer_decorator

    return timer_decorator(_func)

# классическая версия
# def timer_with_precision(precision: int = 1) -> Callable:
#     def timer_decorator(func: Callable) -> Callable:
#         @functools.wraps(func)
#         def wrapped_func(*args, **kwargs) -> Any:
#             # some code
#             value = func(*args, **kwargs)
#             # other code
#             return value
#
#         return wrapped_func
#
#     return timer_decorator
