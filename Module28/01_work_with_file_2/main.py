import os


class File:
    """
    Контекст менеджер для работы с файлами.

    Файл всегда открывается с параметром encoding='utf-8'

    При попытке открытия несуществующего файла, создает его
    и открывает в режиме записи.
    Если 'PermissionError', к имени добавится '_1' и файл
    откроется в режиме записи.
    """
    def __init__(self, file_name: str, mode: str) -> None:
        self.__file_name = file_name
        self.__mode = mode
        self.__encoding = 'utf-8'
        self.__file = None

    def __enter__(self):
        # Если файл не существует, откроем его в режиме записи
        if not os.path.exists(self.__file_name):
            self.__mode = 'w'

        try:
            self.__file = open(self.__file_name, self.__mode, encoding=self.__encoding)

        except PermissionError:
            # если заблокирован, добавим к имени '_1' и откроем для записи
            self.__file_name += '_1'
            self.__mode = 'w'
            self.__file = open(self.__file_name, self.__mode, encoding = self.__encoding)

        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.__file.close()
        return True


def main(f_name):
    file_name = os.path.abspath(os.path.join(os.path.curdir, f_name))

    # Удалим файл, если он существует
    if os.path.exists(file_name):
        os.remove(file_name)

    # и попробуем открыть для чтения
    # вместо этого, он откроется для записи
    # запишем туда строку
    with File(file_name, 'r') as file:
        file.write('Строка текста.\n')

    # теперь прочитаем оттуда
    with File(file_name, 'r') as i_file:
        data = i_file.read()

    # и напечатаем
    print(data)


main('text.txt')
