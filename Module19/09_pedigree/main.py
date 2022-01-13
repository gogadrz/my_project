# Найти родителя.
def find_parent(f_pairs, name):
    parent = 0
    if name not in f_pairs.keys():
        return parent
    else:
        parent = f_pairs[name]
        return parent


# Вычислить поколение
def number_of_generations(g_pairs, name):
    counter = 0
    parent = find_parent(g_pairs, name)
    while parent != 0:
        name = parent
        parent = find_parent(g_pairs, name)
        counter += 1

    return counter


pairs = dict()
generation_dict = dict()
names_set = set()

num_peoples = int(input('Введите количество человек: '))

# Заполнить первоначальный словарь
for i_pair in range(1, num_peoples):
    print('{0} пара: '.format(i_pair), end='')
    p_str = input().split()
    pairs[p_str[0]] = p_str[1]

# И ключи и значения словаря в множество (убрать дубли)
for key in pairs:
    names_set.add(key)
for value in pairs.values():
    names_set.add(value)

# Вычислить поколение и добавить в "готовый" словарь
for _ in range(len(names_set)):
    g_name = names_set.pop()
    generation_dict[g_name] = number_of_generations(pairs, g_name)

# Напечатать с сортировкой
print('\n"Высота" каждого члена семьи:')
for name_gen in sorted(generation_dict):
    print(name_gen, generation_dict[name_gen])
