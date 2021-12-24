def fill_list(f_list, num, count):
    print('Заполняем', num, 'список:')
    for i_num in range(count):
        print('Введите', i_num + 1, 'элемент: ', end = '')
        f_list.append(int(input()))


list_1 = []
list_2 = []

fill_list(list_1, 1, 3)
fill_list(list_2, 2, 7)

print('\nПервый список:', list_1)
print('Второй список:', list_2)

list_1.extend(list_2)
list_2.clear()

for index in list_1:
    if index not in list_2:
        list_2.insert(0, index)

print('\nНовый первый список с уникальными элементами:', list_2)
