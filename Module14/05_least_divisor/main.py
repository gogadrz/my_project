def min_divider(num):
    divider = 2
    while divider <= num:
        if num % divider == 0:
            return divider
        divider += 1
    return num

number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', min_divider(number))
