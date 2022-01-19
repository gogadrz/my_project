import os.path

summ = 0
in_file_name = 'numbers.txt'
out_file_name = 'answer.txt'

path_name_in_file = os.path.abspath(os.path.join(os.path.curdir, in_file_name))

out_file = out_file_name

ifile = open(path_name_in_file, 'r', encoding = 'utf-8')

for i in ifile:
    summ += int(i)

ifile.close()

ofile = open(out_file, 'w')
ofile.write(str(summ))
ofile.close()

# print(summ)

# print(path_name_in_file)