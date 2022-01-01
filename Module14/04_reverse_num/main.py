def reverse_number(num):
    tmp = 0
    while num > 0:
        tmp *= 10
        tmp += num % 10
        num //= 10
    return tmp


def split_number(num):
    x = reverse_number(int(num))
    y = reverse_number(int(round(num - int(num), 2) * 100))
    return x + y / 100


first_number = float(input('Введите первое число: '))
second_number = float(input('Введите второе число: '))

print('\nПервое число наоборот:', split_number(first_number))
print('Второе число наоборот:', split_number(second_number))
print('Сумма:', split_number(first_number) + split_number(second_number))

