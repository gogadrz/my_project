names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day_list = []

for name_index in range(0, len(names_list), 2):
    first_day_list.append(names_list[name_index])

print('Первый день:', first_day_list)
