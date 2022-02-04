import os
from collections.abc import Iterable


def gen_files_path(seek_dir_name: str, start_path: str = None) -> Iterable[str]:
    start_path = start_path or os.path.abspath(os.path.sep)

    for item_name in os.listdir(start_path):
        cur_path = os.path.abspath(os.path.join(start_path, item_name))

        if os.path.isdir(cur_path):
            yield start_path, item_name

            try:
                yield from gen_files_path(seek_dir_name=seek_dir_name, start_path=cur_path)
            except PermissionError:
                print('PermissionError: {}'.format(cur_path))


def seek_dir(seek_dir_name: str, start_path: str = None) -> None:
    gen_flist = gen_files_path(seek_dir_name, start_path)

    for i_path, i_name in gen_flist:
        full_path = os.path.abspath(os.path.join(i_path, i_name))

        if i_name == seek_dir_name:
            print('\nДиректория {dir_name} найдена.\nПолный путь: {full_dir_name}'.format(
                dir_name=i_name,
                full_dir_name=full_path
            ))

            return

        else:
            print(full_path)


def main():

    seek_name = input('Введите имя Директории для поиска: ').lower()
    print()

    seek_dir(seek_dir_name=seek_name, start_path=None)


main()
