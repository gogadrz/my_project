def is_prime(number):
    if number < 2:
        return False
    for i_number in range(number - 1, 1, -1):
        if number % i_number == 0:
            return False
    return True


def get_list(iter_obj):
    return [elem for index, elem in enumerate(iter_obj) if is_prime(index)]


# list
# input_str = ['vasya', 'petr', 'andy', 'anna', 'semen', 'evlamphy', 'makar', 'vakula', 'soso', 'billy']

# tuple (str)
# input_str = ('vasya', 'petr', 'andy', 'anna', 'semen', 'evlamphy', 'makar', 'vakula', 'soso', 'billy')

# tuple (dig)
# input_str = (num for num in range(1, 16))

# dict
# input_str = {'vasya': 20, 'petr': 21, 'andy': 30, 'anna': 18,
#              'semen': 25, 'evlamphy': 97, 'makar': 15, 'vakula': 70}

# string

input_str = 'Папа Карло'
print(get_list(input_str))
