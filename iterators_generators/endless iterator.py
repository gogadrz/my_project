class EndLessIterator:
    def __init__(self, num):
        self.__index = 0
        self.__storage = list(range(num))
        self.__len = len(self.__storage)

    def __iter__(self):
        return self

    def __next__(self):
        value = self.__storage[self.__index]
        self.__index += 1
        self.__index %= self.__len
        return value


my_iter = EndLessIterator(7)

counter = 0
for i in my_iter:
    print(i)
    counter += 1
    if counter >= 20:
        break
