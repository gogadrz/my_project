def shift_string(str_text, step):
    str_lst = list(str_text)
    for _ in range(step):
        sym = str_lst[0]
        str_lst.pop(0)
        str_lst.append(sym)

    shifted_string = ''.join(str_lst)
    return shifted_string


def find_shift(str1, str2):
    for i_shift in range(len(str1)):
        if shift_string(str1, i_shift) == str2:
            return i_shift
    return False


string_1 = input('Первая строка: ')
string_2 = input('Вторая строка: ')

if string_1 != string_2:
    shift = find_shift(string_1, string_2)
    if not shift:
        print('\nПервую строку нельзя получить из второй с помощью циклического сдвига.')
    else:
        print('\nПервая строка получается из второй со сдвигом {0}.'.format(shift))
else:
    print('\nСтроки равны, сдвиг не нужен.')

