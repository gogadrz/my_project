import os
from collections.abc import Iterable


def gen_files_path(seek_dir_name: str, start_path: str = None) -> Iterable[str]:
    start_path = start_path or os.path.abspath(os.path.sep)

    for item_name in os.listdir(start_path):
        cur_path = os.path.abspath(os.path.join(start_path, item_name))

        if os.path.isdir(cur_path):
            if item_name.lower() == seek_dir_name:
                result = '\nКаталог найден.\nПолный путь: {directory}'.format(directory = cur_path)
                print(result)
                return
            else:
                ftype = '<DIR>  '
        else:
            ftype = '<file> '

        ftype_path = ftype + cur_path

        yield ftype_path

    print('Каталог не найден.')
    return False


def main():
    seek_dir = input('Введите имя Директории для поиска: ').lower()

    gen_flist = gen_files_path(seek_dir_name = seek_dir)

    for i_file in gen_flist:
        print(i_file)


main()
