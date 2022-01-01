def main():
    alphabet = 'abcdefg'
    print(' 1: ', alphabet[:], sep = '')
    print(' 2: ', alphabet[::-1], sep = '')
    print(' 3: ', alphabet[::2], sep = '')
    print(' 4: ', alphabet[1::2], sep = '')
    print(' 5: ', alphabet[:1], sep = '')
    print(' 6: ', alphabet[-1:-2:-1], sep = '')
    print(' 7: ', alphabet[3:4], sep = '')
    print(' 8: ', alphabet[-3:], sep = '')
    print(' 9: ', alphabet[3:5], sep = '')
    print('10: ', alphabet[4:2:-1], sep = '')


if __name__ == '__main__':
    main()
