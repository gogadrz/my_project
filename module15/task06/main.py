word_as_list = []


def count_letter(sym_list, sym):
    counter = 0
    for symbol in sym_list:
        if symbol == sym:
            counter += 1
    return counter


def calculate_unique_letters(sym_list):
    counter = 0
    for symbol in sym_list:
        if count_letter(sym_list, symbol) == 1:
            counter += 1
    return counter


word = input('Введите слово: ')
word_as_list = list(word)

print('Количество уникальных букв:', calculate_unique_letters(word_as_list))
