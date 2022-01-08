synonyms_dict = dict()

pairs_num = int(input('Введите количество пар слов: '))

for i_pairs in range(1, pairs_num + 1):
    print('{0} пара: '.format(i_pairs), end='')
    synonyms = input().title().split(' - ')

    synonyms_dict[synonyms[0]] = synonyms[1]

print()

done = False
while not done:
    word = input('Введите слово: ').title()

    if word in synonyms_dict:
        print('Синоним:', synonyms_dict[word])
        done = True
    elif word in synonyms_dict.values():
        for itm in synonyms_dict.items():
            if itm[1] == word:
                print('Синоним:', itm[0])
                done = True
    else:
        print('Такого слова в словаре нет.')
