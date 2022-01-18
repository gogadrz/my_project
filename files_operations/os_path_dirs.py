import os

file_name = 'gogadrz.txt'
folder = 'g_project'

# полный путь к текущей директории
full_path = os.path.abspath('')
print(full_path)

# полный путь к папке и имя файла
full_path = os.path.abspath(file_name)
print(full_path)

# на уровень выше и в "Python_Basic" с именем файла
full_path = os.path.abspath(os.path.join('../..', 'Python_Basic', file_name))
print(full_path)

# разделитель. то есть в корень диска
full_path = os.sep
print(full_path)

# список файлов текущей директории
directory = os.path.abspath('')
for f_name in os.listdir():
    full_fname = os.path.join(directory, f_name)
    print(full_fname)


directory = 'access'
f_name = 'admin.bat'

full_path = os.path.abspath(os.path.join(directory, f_name))
print('полный путь', full_path)

full_path = os.path.join(os.path.sep, directory, f_name)
print('относительный путь к файлу', full_path)

path_to_file = os.path.abspath('')
for f_name in os.listdir():
    print(os.path.join(path_to_file, f_name), end = '')
    if os.path.isdir(f_name):
        print(os.path.sep, end = '')
    print()

# родительская директория
parent_path = os.path.abspath(os.path.join(path_to_file, os.pardir))
parent_path_on_2_levels = os.path.abspath(
    os.path.join(os.path.abspath(os.path.join(path_to_file, os.pardir)), os.pardir))
print(parent_path)

# ну или
parent_path = os.path.abspath(os.path.join('../..', 'file.txt'))
print(parent_path)
