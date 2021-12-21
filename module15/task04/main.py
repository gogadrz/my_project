cards_count = int(input('Количество видеокарт: '))
cards_old_list = []
cards_new_list = []
newest_model = 0

for index in range(cards_count):
    print(index + 1, 'Видеокарта: ', end="")
    card = int(input())
    if card > newest_model:
        newest_model = card
    cards_old_list.append(card)

for card in cards_old_list:
    if card != newest_model:
        cards_new_list.append(card)


print('\nСтарый список видеокарт:', cards_old_list)
print('Новый список видеокарт:', cards_new_list)
