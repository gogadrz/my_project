import random

min_dig = random.randint(0, 30)
max_dig = random.randint(0, 30)
work_list = [index for index in range(1, 30 + 1)]

print('min = ', min_dig, '\tmax = ', max_dig)
print('основной список', work_list)

if min_dig > max_dig:
    min_dig, max_dig = max_dig, min_dig

print('min = ', min_dig, '\tmax = ', max_dig)

work_list = [item for item in work_list if not min_dig <= item <= max_dig]


print('основной список после обработки', work_list)
