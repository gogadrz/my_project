def print_set(printed_set):
    for i_set in sorted(printed_set):
        print(i_set, end=' ')
    return


max_num = int(input('Введите максимальное число: '))
result_set = set()

while True:
    print('\nНужное число есть среди вот этих чисел: ', end='')
    inp_text = input()
    if inp_text.title() == 'Помогите!':
        print('Артём мог загадать следующие числа: ', end='')
        print_set(result_set)
        break
    else:
        dig_lst = inp_text.split()

        print('Ответ Артёма: ', end='')
        answer = input().title()
        if answer == "Да":
            result_set.update(dig_lst)
        elif answer == "Нет":
            result_set -= set(dig_lst)
        else:
            pass
