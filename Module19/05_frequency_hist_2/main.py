sym_dict = dict()
inverse_sym_dict = dict()

text = input('Введите текст: ')

for sym in text:
    if sym in sym_dict:
        sym_dict[sym] += 1
    else:
        sym_dict[sym] = 1

print('Оригинальный словарь частот:')

for itm in sorted(sym_dict):
    print(itm, ':', sym_dict[itm])

print('\nИнвертированный словарь частот:')

for index_list in range(1, max(sym_dict.values()) + 1):
    inverse_sym_dict[index_list] = []

for key, value in sym_dict.items():
    if key not in inverse_sym_dict[value]:
        inverse_sym_dict[value].append(key)

for i_lst in inverse_sym_dict.keys():
    print(i_lst, ':', inverse_sym_dict[i_lst])
