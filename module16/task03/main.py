shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500],
        ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]

part_name = input('Название детали: ')
part_cnt = 0
part_sum = 0

for i_shop in shop:
    if i_shop[0] == part_name:
        part_cnt += 1
        part_sum += i_shop[1]

print('\nКол-во деталей -', part_cnt)
print('Общая стоимость -', part_sum)
