order_dict = dict()
dishes_set = set()
order_nums = int(input('Введите кол-во заказов: '))

for i_orders in range(1, order_nums + 1):
    print('{0} заказ: '.format(i_orders), end='')
    order_lst = input().title().split()
    order_lst[2] = int(order_lst[2])

    # если фамилии нет - добавить полную запись
    if order_lst[0] not in order_dict:
        order_dict[order_lst[0]] = [{order_lst[1]: order_lst[2]}]
    else:

        # фамилия есть, а есть ли это блюдо?
        for dish_key in order_dict[order_lst[0]][0].keys():

            # список блюд клиента
            dishes_set.add(dish_key)
        if order_lst[1] in dishes_set:

            # блюдо тоже есть, изменим количество
            order_dict[order_lst[0]][0][order_lst[1]] += order_lst[2]
        else:
            # блюдо клиент не заказывал, добавим ему блюдо и количество
            order_dict[order_lst[0]][0][order_lst[1]] = order_lst[2]

print()
for i_client in sorted(order_dict.keys()):
    print('{0}:'.format(i_client))
    for i_dish in sorted(order_dict[i_client][0].keys()):
        print('\t{0}: {1}'.format(i_dish, order_dict[i_client][0][i_dish]))
