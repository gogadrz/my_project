def main():
    len_list = int(input('Введите длину списка: '))
    digits_list = [1 if index % 2 == 0 else index % 5 for index in range(len_list)]
    print('Результат:', digits_list)


if __name__ == '__main__':
    main()

