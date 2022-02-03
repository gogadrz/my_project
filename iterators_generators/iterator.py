import random


class RandomNumbers:
    def __init__(self, limit):
        self.__limit = limit
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__limit:
            self.__counter += 1
            return random.randint(1, 10)
        else:
            raise StopIteration


my_iter = RandomNumbers(limit=3)

for rand_val in my_iter:
    print(rand_val)
