def fix_index(cur_index, max_list_index):
    if cur_index > max_list_index:
        cur_index = cur_index % (max_list_index + 1)
    return cur_index


def next_outer(cur_index, step, max_list_index):
    next_index = 0
    for index in range(step):
        next_index = fix_index(cur_index + index, max_list_index)
    return next_index


def print_report(current_list, current_number, get_out):
    print('\nТекущий круг людей:', current_list)
    print('Начало счёта с номера', current_number)
    print('Выбывает человек под номером', get_out)


gamers_count = int(input('Кол-во человек: '))
gamers_list = list(range(1, gamers_count + 1))
step = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', step, 'человек')
cur_number = 0
max_list_index = gamers_count - 1
outer = 0

while max_list_index > 0:
    cur_number = outer
    outer = next_outer(cur_number, step, max_list_index)
    if cur_number > max_list_index:
        cur_number = 0
    print_report(gamers_list, gamers_list[cur_number], gamers_list[outer])
    gamers_list.pop(outer)
    max_list_index -= 1

print('\nОстался человек под номером', gamers_list[0])
