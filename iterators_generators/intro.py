items = [10, 20, 30, 40, 50]

# iterator = items.__iter__()
iterator = iter(items)

# for elem in iterator:
#     print(elem)

while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        print('Конец итерируемого объекта')
        break

# когда итератор прошел по всему списку, его следующий вызов выбросит исключение StopIteration
