# Здравствуйте Александр.
# К сожалению я поздно заметил что код буквы 'ё' находится вне диапазона алфавита.
# В примере по задаче её нет. Но если нужно я перепишу функцию,
# что бы с 'ё' все работало корректно.
#
def next_sym(symbol, step):
    if not ord('я') > ord(symbol) > ord('а'):
        return symbol
    else:
        symbol = chr(ord(symbol) + step)
        if ord(symbol) - ord('а') > ord('я') - ord('а'):
            symbol = chr(ord(symbol) - (ord('я') - ord('а') + 1))
        return symbol


def main():
    message = list(input('Введите сообщение: '))
    shift = int(input('Введите сдвиг: '))

    print('Зашифрованное сообщение: ', end = '')

    for letter in message:
        print(next_sym(letter, shift), end = '')


if __name__ == '__main__':
    main()
