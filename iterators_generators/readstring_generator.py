def get_data():
    with open('numbers.txt', 'r') as input_file:

        str_data = input_file.readline()
        while str_data:
            yield str_data
            str_data = input_file.readline()


in_str_generator = get_data()

print(in_str_generator.__next__())
print(in_str_generator.__next__())
print(in_str_generator.__next__())

for line in in_str_generator:
    print(line.strip())
