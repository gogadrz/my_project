from typing import Callable, Any
import functools


def check_permission(user: str) -> Callable:
    """
    Декоратор.
    Проверяет есть ли у пользователя доступ к вызываемой функции,
    если нет, то выдает исключение PermissionError
    """

    def decorator(func: Callable) -> Callable:

        @functools.wraps(func)
        def wrapped(*args, **kwargs) -> Any:

            user_permissions = ['admin']
            if user not in user_permissions:
                value = False
                try:
                    raise PermissionError

                except PermissionError:
                    print('PermissionError: У пользователя недостаточно прав, чтобы выполнить функцию add_comment')
            else:
                value = func(*args, **kwargs)

            return value
        return wrapped
    return decorator


def main():
    # Здравствуйте Александр.
    # Я позволил себе перенести "user_permissions = ['admin']" в тело обёртки.
    # Мог бы передать декоратору в виде параметра. В примере эта строка в основном коде,
    # а я не знаю как её "увидеть" из обёртки.
    # Подскажите, как надо было сделать? Спасибо.

    @check_permission('admin')
    def delete_site():
        print('Удаляем сайт')

    @check_permission('user_1')
    def add_comment():
        print('Добавляем комментарий')

    delete_site()
    add_comment()


main()
