def tuple_slice(tpl, sym):
    result_str = ''
    to_str = False
    if sym not in tpl:
        return ()
    else:
        for item in tpl:
            if item == sym:
                if to_str == False:
                    to_str = True
                else:
                    result_str += item
                    to_str = False
            if to_str:
                result_str += item

    return tuple(result_str)
# row = [unicode(x.strip()) for x in row if x is not None else '']
[item
    if to_str item
    for item in tpl

 ]
# В условии ничего не сказано как должна вести себя эта функция
# если "случайных элементов" окажется больше двух. Поэтому такую ситуацию
# я не обрабатывал.
#
some_tuple = tuple('абв1где2ёе1д3гвба')
slice_sym = input('Введите символ для среза: ')

print(tuple_slice(some_tuple, slice_sym))
