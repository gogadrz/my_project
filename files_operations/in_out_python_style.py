import os
 

def line_analysis(line):
    line = line.strip()
    res = 0

    if len(line) > 0:
        res = int(line.strip())
    return res

def get_file_path(file_name):
    return os.path.abspath(os.path.join('.', file_name))

def get_lines(file_name):
    file_path = get_file_path(file_name)
    out = []

    with open(file_path, 'r') as input_file:
        out += input_file.readlines()[::-1]

    return out


def output(result, file_name):
    file_path = get_file_path(file_name)
    with open(file_path, 'w') as output_file:
        output_file.write(str(result))

def main(input_filename, output_filename):
    result = 0

    for line in get_lines(input_filename):
        result += line_analysis(line)

    output(result, output_filename)

main('numbers.txt', 'answer.txt')