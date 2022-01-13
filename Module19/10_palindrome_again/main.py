text_dict = dict()
odd_cnt_letter = 0
text = input('Введите строку: ')

for symbol in text:
    if symbol in text_dict:
        text_dict[symbol] += 1
    else:
        text_dict[symbol] = 1

for cnt_sym in text_dict.values():
    if cnt_sym % 2 != 0:
        odd_cnt_letter += 1

if odd_cnt_letter > 1:
    print('Нельзя сделать палиндромом')
else:
    print('Можно сделать палиндромом')
