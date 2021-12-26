left = 5
right = 10

cubes_list = [(left + x) ** 3 for x in range(right - left + 1)]
square_list = [(left + x) ** 2 for x in range(right - left + 1)]


print(cubes_list)
print(square_list)
print(sum(cubes_list))
