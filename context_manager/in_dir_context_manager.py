from contextlib import contextmanager
import os


@contextmanager
def in_dir(path: str) -> None:

    print('Inside context manager')
    save_path = os.path.abspath(os.path.curdir)
    new_path = os.path.abspath(os.path.join(os.path.curdir, path))

    try:

        if not os.path.exists(new_path):
            raise FileExistsError

        print('Меняем текущую директорию на: {}'.format(new_path))
        os.chdir(new_path)

        yield

    except FileExistsError:
        yield
        print('Ошибка: Указанный путь не найден!')
        print('Директория не изменена!')
        return True

    else:
        print('Восстанавливаем текущую директорию')
        os.chdir(save_path)


def main():
    print('До контекст менеджера')
    print(os.listdir())

    with in_dir('c:\\фыв'):
        print('В контекст менеджере')
        print(os.listdir())

    print('После контекст менеджера')
    print(os.listdir())


main()
