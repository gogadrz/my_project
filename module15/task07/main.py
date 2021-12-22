def calculate_new_container_index(weight):
    for index in range(len(containers)):
        if containers[index] < weight:
            return index


def input_valid(number):
    if number <= 200:
        return True
    else:
        return False


def input_data(prompt):
    print(prompt, end = '')
    number = int(input())
    while not input_valid(number):
        print('Ошибка ввода. Попробуйте еще раз.')
        print(prompt)
        number = int(input())
    return number


container_count = input_data('Количество контейнеров: ')
containers = []
new_container_weight = 0

for _ in range(container_count):
    container_weight = input_data('Введите вес контейнера: ')
    containers.append(container_weight)

new_container_weight = input_data('Введите вес нового контейнера: ')

print('Номер, который получит новый контейнер:', calculate_new_container_index(new_container_weight))
