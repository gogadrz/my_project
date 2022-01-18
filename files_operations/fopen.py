# если будет кириллица, то нужен параметр encoding='utf-8'
speakers_file = open('speakers.txt', 'r', encoding='utf-8')

# data = speakers_file.read()
# print(data)

for line in speakers_file:
    print(line, end='')



speakers_file.close()

