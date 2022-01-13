print('Введите координаты монетки:')
x_coin = float(input('X: '))
y_coin = float(input('Y: '))
radius = float(input('Введите радиус: '))

if x_coin ** 2 + y_coin ** 2 <= radius ** 2:
    print('\nМонетка где-то рядом')
else:
    print('\nМонетки в области нет')

