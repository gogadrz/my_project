from typing import Callable, Any


def decorator(func: Callable) -> Callable:
    def wrapped_func(*args, **kwargs) -> Any:
        print('</----------\>')
        value = func(*args, **kwargs)
        print('<\______/>')
        return value

    return wrapped_func


@decorator
def sandwich() -> None:
    print('#помидоры#')
    print('--ветчина--')
    print('~салат~')


sandwich()
