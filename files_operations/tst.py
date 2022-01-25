import os


def get_file_path(file_name):
    return os.path.abspath(os.path.join(os.path.curdir, file_name))


def get_lines(file_name):
    file_path = get_file_path(file_name)
    out_data = list()

    try:
        with open(file_path, 'r') as input_file:
            out_data += input_file.readlines()[:]
    except IsADirectoryError:
        print('it directory')
    except BaseException:
        print('unknown error')

    return out_data


def output(out_file_name, result):
    file_path = get_file_path(out_file_name)

    if os.path.exists(file_path):
        print(f'Файл \'{out_file_name}\' уже существует и будет перезаписан!')

    with open(file_path, 'w') as output_file:
        output_file.writelines(result)


def main(in_file_name, out_file_name):
    result = []
    for index, line in enumerate(get_lines(in_file_name)):
        f_string = '{0} {1}'.format(chr(index + ord('a')), line)
        result.append(f_string)

    output(out_file_name, result)
    return


main('ages.txt', 'result.txt')
