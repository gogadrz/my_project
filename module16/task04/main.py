def add_guest(added_guest):
    added_name = input('Имя гостя: ').capitalize()
    if len(added_guest) < 6:
        print('Привет, ', added_name, '!', sep = '')
        added_guest.append(added_name)
    else:
        print('Прости, ', added_name, ', но мест нет.', sep = '')


def remove_guest(rem_guest):
    if len(rem_guest) == 0:
        print('На вечеринке никого нет.')
        return
    rem_name = input('Имя гостя: ').capitalize()
    for i_rem_name in rem_guest:
        if i_rem_name == rem_name:
            rem_guest.remove(i_rem_name)
            print('Пока, ', rem_name, '!', sep = '')
            return
    print('Гостя по имени ', rem_name, ' нет на вечеринке.')


def menu():
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    cmd = input('Гость пришёл или ушёл? ').capitalize()
    return cmd


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
max_guests = 6
command = ''

while command != 'Пора спать':
    command = menu()

    if command == 'Пришёл' or command == 'Пришел':
        add_guest(guests)
    elif command == 'Ушёл' or command == 'Ушел':
        remove_guest(guests)

print('Вечеринка закончилась, все легли спать.')

