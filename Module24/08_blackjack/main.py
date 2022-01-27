from classes import CardDeck, Player


def main():

    debug = False

    name = input('Введите Ваше имя: ')
    if name == '':
        name = 'Player'

    print()

    cards_deck = CardDeck()

    dealer = Player('Дилер')
    gamer = Player(name)

    dealer.add_card(cards_deck.get_card())
    dealer.add_card(cards_deck.get_card())
    gamer.add_card(cards_deck.get_card())
    gamer.add_card(cards_deck.get_card())

    while True:
        gamer.info()
        if debug:
            dealer.info()

        if gamer.score == 21:
            print('Глупый вопрос,')

        answer = input('Вы будете брать еще карту (1: да, 2: нет)? ')

        if answer == '2':
            break

        elif answer == '1':
            gamer.add_card(cards_deck.get_card())

            if gamer.score > 21 or dealer.score > 21:
                break

    if gamer.score > 21:
        print('\nВы сгорели!\n')

    elif gamer.score == dealer.score:
        print('\nКаждый остается при своих.\n')

    elif gamer.score > dealer.score:
        print('\n{} выиграл!\n'.format(gamer.name))

    else:
        print('\n{} выиграл!\n'.format(dealer.name))

    print('-' * 52)
    gamer.info()
    print('-' * 52)
    dealer.info()


main()
