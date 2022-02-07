from typing import Callable


PLUGINS = dict()


def register():
    pass


def say_hello(name: str) -> str:
    return 'Hello {name}'.format(name=name)


def say_goodbye(name: str) -> str:
    return 'Goodbye {name}'.format(name=name)


