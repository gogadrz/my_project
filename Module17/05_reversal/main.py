def main():
    src_string = input('Введите строку: ')
    start_index = src_string.find('h')
    end_index = src_string.rfind('h') - 1

    # print('start -', start_index, 'end -', end_index)
    print('Развернутая последовательность между первым и последним h:', src_string[end_index:start_index:-1])


if __name__ == '__main__':
    main()
