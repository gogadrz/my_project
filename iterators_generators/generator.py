def fibonacci(number):
    cur_val = 0
    next_val = 1

    for _ in range(number):
        yield cur_val
        cur_val, next_val = next_val, cur_val + next_val

# а это просто генератор значений по порядку
def hz():
    i = 0
    while True:
        yield i
        i += 1


x = hz()
for j in range(200):
    print(x.__next__())

fib_seq = fibonacci(number = 10)

# for i_value in fib_seq:
#     print(i_value)

# print(fib_seq.__next__())
# print(fib_seq.__next__())
# print(fib_seq.__next__())
# print(fib_seq.__next__())
# print(fib_seq.__next__())
# print(fib_seq.__next__())
# print(fib_seq.__next__())
