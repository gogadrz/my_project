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
full_path = os.path.abspath(os.path.join('..', 'Python_Basic', file_name))
print(full_path)

# разделитель. то есть в корень диска
full_path = os.sep
print(full_path)

# список файлов текущей директории
directory = os.path.abspath('')
for f_name in os.listdir():
    full_fname = os.path.join(directory, f_name)
    print(full_fname)
