import os


def search_file(cur_path, file_name):
    print('Переходим в', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        print('    смотрим -', i_elem)
        if file_name == i_elem:
            return path
        if os.path.isdir(path):
            print('<DIR>', i_elem)
            result = search_file(path, file_name)
            if result:
                break
    else:
        result = None

    return result

search_path = os.path.abspath(os.path.join(os.path.abspath(''), os.pardir, 'Python_Basic'))
# search_path = os.path.join(os.path.sep, 'test')
file_name = 'main.py'

result = search_file(search_path, file_name)
if result:
    print('полный путь к файлу: ', result)
else:
    print('в указанном пути файл не найден')

