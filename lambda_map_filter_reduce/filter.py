nums = [i for i in range(15)]

print(nums)

even = list(filter(lambda x: x % 2 == 0, nums))
print(even)


# можно map вместе с filter использовать:
result = list(map(lambda num: num * 3, filter(lambda num: num % 2, nums)))

print(result)

# возвращаются все истинные значения
# filter(None, nums)
