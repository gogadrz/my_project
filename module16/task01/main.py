main_list = [1, 5, 3]
secondary1_list = [1, 5, 1, 5]
secondary2_list = [1, 3, 1, 5, 3, 3]


def chg_lst(lst1, lst2, dig):
    lst1.extend(lst2)
    dig_cnt = lst1.count(dig)
    print('Кол-во цифр', dig, 'при первом объединении:', dig_cnt)
    return dig_cnt


for _ in range(chg_lst(main_list, secondary1_list, 5)):
    main_list.remove(5)
chg_lst(main_list, secondary2_list, 3)

print(main_list)
