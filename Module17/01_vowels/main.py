def main():
    vowels_list = ['а', 'и', 'е', 'ё', 'о', 'у', 'ы', 'э', 'ю', 'я']
    changed_list = []

    text = list(input('Введите текст: '))
    for i_text in text:
        if i_text in vowels_list:
            changed_list.append(i_text)

    print('\nСписок гласных букв:', changed_list)
    print('Длина списка:', len(changed_list))


if __name__ == '__main__':
    main()
