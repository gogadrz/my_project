def sum_digits(num):
    count = 0
    while num > 0:
        count += num % 10
        num //= 10
    return count


def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


number = int(input('Введите число: '))

print('Сумма цифр:', sum_digits(number))
print('Кол-во цифр в числе:', count_digits(number))
print('Разность суммы и кол-ва цифр:', sum_digits(number) - count_digits(number))
