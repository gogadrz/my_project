import itertools

colors = ['красный', 'желтый', 'зеленый', 'синий']

# все варианты без повторений, порядок важен
for item in itertools.permutations(colors, 2):
    print(item)

print('*' * 40)
# все комбинации (сочетания) порядок не важен
for item in itertools.combinations(colors, 2):
    print(item)

print('*' * 40)
# кольцевой итератор
iterator = itertools.cycle(['раз', 'два', 'три'])
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

