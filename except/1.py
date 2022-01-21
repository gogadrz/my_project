def main(i_file):
    out = []
    with open(i_file, 'r') as in_file:
        out += in_file.readlines()[::-1]
    if out:
        summ = 0
        for i in out:
            print(i.strip())
            summ += int(i.strip())
    print(summ)




main('ages.txt')
