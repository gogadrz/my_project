class Fibonacci:

    def __init__(self, number):
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        self.number = number

    def __iter__(self):
        # что бы после цикла (опустошения итератора) при следующем доступе не поймать StopIteration,
        # обнулим все значения.
        self.counter = 0
        self.cur_val = 0
        self.next_val = 1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter > 1:
            if self.counter > self.number:
                raise StopIteration()
            self.cur_val, self.next_val = self.next_val, self.cur_val + self.next_val

        return self.cur_val


# Lazy evaluation - ленивое вычисление. Только то что надо, а не сразу все значения.

fib_iterator = Fibonacci(10)

for i_value in fib_iterator:
    print(i_value)

print(8 in fib_iterator)
