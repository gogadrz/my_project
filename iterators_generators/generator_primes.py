def get_next_prime(limit):
    last_prime = 0
    for index in range(last_prime + 1, limit + 1):
        if check_prime(index):
            yield index


def check_prime(number):
    if number < 2:
        return False
    count = 0
    for index in range(1, number):
        if number % index == 0:
            count += 1

    if count < 2:
        return True
    else:
        return False


generator = get_next_prime(10)

for value in generator:
    print(value)
