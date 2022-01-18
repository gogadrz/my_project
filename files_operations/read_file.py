import os

f_name_1 = 'group_1.txt'
f_name_2 = 'group_2.txt'
sum_results = 0
file_1_path = os.path.abspath(os.path.join(os.path.curdir, 'task', f_name_1))
file_2_path = os.path.abspath(os.path.join(os.path.curdir, 'task', 'additional_info', f_name_2))

file_1 = open(file_1_path, 'r', encoding='utf-8')

for i in file_1:
    _, _, result = i.split()
    sum_results += int(result)

file_1.close()

print('сумма результатов первого файла', sum_results)

file_1 = open(file_1_path, 'r', encoding='utf-8')

sum_results = 0
for i in file_1:

    _, _, result = i.split()
    sum_results -= int(result)

file_1.close()

print('разность результатов первого файла', sum_results)

file_2 = open(file_2_path, 'r', encoding='utf-8')

sum_results = 1
for i in file_2:

    _, _, result = i.split()
    sum_results *= int(result)

file_2.close()

print('произведение результатов второй группы', sum_results)