def check_palindrom(word):
    word_as_list = list(word)

    for index in range(len(word_as_list) // 2):
        back_index = -index - 1
        if word_as_list[index] != word_as_list[back_index]:
            return False

    return True

word = input('Введите слово: ')

if check_palindrom(word):
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')
