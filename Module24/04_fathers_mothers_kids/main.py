from parent_chdren import Parent, Child


parent = Parent('Отец Фёдор', 30, [Child('Сережа', 3, crying=True),
                                   Child('Лена', 4, hungry=True),
                                   Child('Виталик', 18)])

parent.show_info()

print('Виталик не подошел по возрасту, осталось двое детей, Сережа и Лена')
print('Сережа плачет, Лена хочет есть')
print('Успокоим Сережу\n')

parent.soothe_the_child('Сережа')
parent.show_info()

print('И покормим Лену\n')
parent.feed_the_baby('Лена')
parent.show_info()
