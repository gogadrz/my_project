import os


def search_file(cur_path, result = None):
    result = result or list()

    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if not os.path.isdir(path):
            result.append(i_elem)

    return result


search_path = os.path.abspath(os.path.curdir)
res = search_file(search_path)
print(res)

out_file = open('scripts.txt', 'a', encoding = 'utf-8')

for i_name in res:
    ifile = open(i_name, 'r', encoding = 'utf-8')
    data = ifile.read()
    print('\n\nfile ->', i_name)
    print(data)
    print('\n', '*' * 40, '\n')

    fstr = f'file -> {i_name}\n'

    out_file.write(fstr)

    out_file.write(data)
    out_file.writelines('\n\n****************************************\n\n')
    ifile.close()

out_file.close()

