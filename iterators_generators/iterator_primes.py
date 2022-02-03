class Primes:

    def __init__(self, limit):
        self.__limit = limit
        self.__last_prime = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.get_next_prime()
        if value in range(self.__limit):
            self.__last_prime = value
            return value
        else:
            raise StopIteration()

    def get_next_prime(self):
        for index in range(self.__last_prime + 1, self.__limit + 1):
            if self.__check_prime(index):
                return index

    @staticmethod
    def __check_prime(number):
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


prime_nums = Primes(50)

for i_elem in prime_nums:
    print(i_elem, end = ' ')
