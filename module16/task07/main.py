def fill_list(added_list, msg_1, msg_2, msg_3):
    print('\nКол-во ', msg_1, ': ', sep = '', end = '')
    cnt = int(input())

    for i_list in range(cnt):
        print(msg_2, ' ', i_list + 1, ' ',  msg_3, ': ', sep = '', end = '')
        to_list = int(input())
        added_list.append(to_list)


rol_skates_list = []
size_list = []
total_skating = 0

fill_list(rol_skates_list, 'коньков', 'Размер', 'пары')
fill_list(size_list, 'людей', 'Размер ноги', 'человека')

for i_size in size_list:
    for i_skates in rol_skates_list:
        if i_skates == i_size:
            rol_skates_list.remove(i_skates)
            total_skating += 1

print('\nНаибольшее кол-во людей, которые могут взять ролики:', total_skating)
