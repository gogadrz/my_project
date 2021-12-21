n_list = []
n_max = int(input("Введите число: "))

for i in range(1, n_max + 1, 2):
    n_list.append(i)

print('Список из нечётных чисел от одного до N:', n_list)