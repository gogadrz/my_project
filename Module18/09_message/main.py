def words(msg, offset):
    result = ''
    while True:
        sym = msg[offset]
        if sym.isalpha():
            result += msg[offset]
            offset += 1
        else:
            break
    return result, offset


def delimeters(msg, offset):
    result = ''
    while True:
        sym = msg[offset]
        if not sym.isalpha():
            result += msg[offset]
            offset += 1
        else:
            break
    return result, offset


message = input('Сообщение: ')
print('Новое сообщение: ', end='')

peace_of_string = ''
i_char = 0

while i_char < len(message) - 1:
    if message[i_char].isalpha():
        peace_of_string, i_char = words(message, i_char)
        print(peace_of_string[::-1], end='')
    else:
        peace_of_string, i_char = delimeters(message, i_char)
        print(peace_of_string, end='')

print(message[-1])
