max_word = max(input('Введите строку: ').split(), key=len)

print('Самое длинное слово: {}'.format(max_word))
print('Длина этого слова: {}'.format(len(max_word)))
