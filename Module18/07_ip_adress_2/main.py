def is_digit_list(ip_list):
    for num in ip_list:
        if not num.isdigit():
            print(num, end='')
            return False
    return True


def digits_in_range(ip_list):
    for num in ip_list:
        if not 0 <= int(num) <= 255:
            print(num, end='')
            return False
    return True


ip_string = input('Введите IP: ')

ip = ip_string.split('.')
if len(ip) != 4:
    print('Адрес - это четыре числа, разделенные точками')
elif not is_digit_list(ip):
    print(' - не целое число')
elif not digits_in_range(ip):
    print(' превышает 255')
else:
    print('IP-адрес корректен')
