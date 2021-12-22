def shift_list(shift):
    if shift > len(initial_list):
        return False
    else:
        for index in range(-shift, len(initial_list) - shift):
            changed_list.append(initial_list[index])

        return True


def fill_list():
    count = int(input('Сколько элементов будет в списке? '))

    for index in range(count):
        print(index + 1, 'элемент: ', end = '')
        number = int(input())
        initial_list.append(number)


initial_list = []
changed_list = []

fill_list()

shift = int(input('На сколько сдвинуть? '))
if shift_list(shift):
    print('Изначальный список:', initial_list)
    print('Сдвинутый список:', changed_list)
else:
    print('Ошибка. Сдвиг не должен быть больше количества элементов списка.')
