numbers_list = [1, 4, -3, 0, 10]


def sorting_list():
    for index in range(0, len(numbers_list) - 1):
        if numbers_list[index] > numbers_list[index + 1]:
            numbers_list[index], numbers_list[index + 1] = numbers_list[index + 1], numbers_list[index]


def check_sort_list():
    for index in range(0, len(numbers_list) - 1):
        if numbers_list[index] > numbers_list[index + 1]:
            return False
    return True


def sort_list():
    while not check_sort_list():
        sorting_list()


print('Изначальный список:', numbers_list)
sort_list()
print('Отсортированный список:', numbers_list)
