cell_count = int(input('Количество клеток: '))
cells = []

for index in range(cell_count):
    print('Эффективность', index + 1, 'клетки: ', end='')
    cell = int(input())
    if cell < index:
        cells.append(cell)

print('Неподходящие значения: ', end="")

for index in cells:
    print(index, end=' ')
