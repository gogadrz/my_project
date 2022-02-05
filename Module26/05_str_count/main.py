import os
from collections.abc import Iterable


def get_file_list() -> Iterable[str]:
    for i_file in os.listdir():
        yield i_file


def get_data(debug: bool) -> Iterable[str]:

    file = get_file_list()

    for i_file in file:
        if i_file[-3:].strip() != '.py':
            if debug:
                print('--- Файл {file_name} --> пропущен'.format(file_name=i_file))

        else:
            if debug:
                print('--- Файл \'{file_name}\' --> считаем строки...'.format(file_name=i_file))

            with open(i_file, 'r') as in_file:
                for text_line in in_file:
                    yield text_line

    # Some comment
    # --- // ----
    # --- // --- // ---


def calc_total_lines(debug: bool) -> int:
    str_data = get_data(debug)
    counter = 0

    for line in str_data:
        if line.strip() and ('#' not in line):
            counter += 1
            if debug:
                print(counter, line, end='')

    return counter


def main():
    debug = True

    print('\nОбщее количество строк: {total_lines}.'.format(
        total_lines=calc_total_lines(debug=debug)
    ))


main()
