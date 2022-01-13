def sym_count(text_str, position):
    repeater = 0
    while text_str[position] == text_str[position + repeater]:
        repeater += 1
    return repeater


text = input('Введите строку: ')
print('Закодированная строка: ', end='')

index = 0
while index < len(text) - 1:
    print(text[index], sym_count(text, index), sep='', end='')
    index += sym_count(text, index)

print(text[-1], '1', sep='')
