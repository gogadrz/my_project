# генерируем первый класс
first_class = list(range(160, 177, 2))

# генерируем второй класс
second_class = list(range(162, 181, 3))

# объединяем
first_class.extend(second_class)

# сортируем
first_class.sort()

# и выводим
print('Отсортированный список:', first_class)