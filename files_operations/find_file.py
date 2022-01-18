import os
import random


def search_file(cur_path, file_name, result=None):
    result = result or list()
    # print('Переходим в', cur_path)

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        # print('    смотрим -', i_elem)
        if file_name == i_elem:
            # return path
            # print(path)
            result.append(path)
        if os.path.isdir(path):
            # print('<DIR>', i_elem)
            result.extend(search_file(path, file_name))
            # if result:
            #     break
    # else:
    #     result = None

    # return result
    return result

# result = list()
search_path = os.path.abspath(os.path.join(os.path.curdir, '', 'task'))
file_name = 'group_1.txt'
res = search_file(search_path, file_name)

fn = res[random.randint(0, len(res) - 1)]
f = open(fn, 'r', encoding='utf-8')
data = f.read()
f.close()
print(data)


# result = search_file(search_path, file_name)
# if result:
#     print('полный путь к файлу: ', result)
# else:
#     print('в указанном пути файл не найден')


