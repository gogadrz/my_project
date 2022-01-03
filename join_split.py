while True:
    grats_template = input('Введите шаблон поздравления, '
                           'в шаблоне нужно использовать конструкцию '
                           '{name} и {age}: '
                           )

    if '{name}' in grats_template and '{age}' in grats_template:
        break
    print('Ошибка, отсутствует инструкция {name} или {age}!')

names_list = input('Список людей через запятую: ').split(', ')
ages_str = input('Возраст людей через пробел: ')
ages_list = [int(i_number) for i_number in ages_str.split()]

for i_man in range(len(names_list)):
    print(grats_template.format(name=names_list[i_man], age=ages_list[i_man]))

peoples_lst = [
    (' '.join([names_list[i_man], str(ages_list[i_man])]))
    for i_man in range(len(names_list))
]

print(peoples_lst)
print(', '.join(peoples_lst))
