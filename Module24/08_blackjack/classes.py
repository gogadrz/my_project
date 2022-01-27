import random


class Card:
    suits_dict = {0: 'clubs', 1: 'diamonds', 2: 'hearts', 3: 'spades'}

    def __init__(self, name, price, suit):
        self.name = name
        self.price = price
        self.suit = suit

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def info(self):
        print('{:>10},  масть: {:>8},  ценовое значение: {:2}'.format(
            self.name,
            self.suits_dict[self.suit],
            self.price
        ))


class CardDeck:

    def __init__(self):
        self.deck = []

        for i_suit in range(4):
            self.deck.extend([Card(str(index), index, i_suit) for index in range(2, 11)])
            self.deck.append(Card('Ace', 11, i_suit))
            self.deck.append(Card('Queen', 10, i_suit))
            self.deck.append(Card('Jack', 10, i_suit))
            self.deck.append(Card('King', 10, i_suit))

            random.shuffle(self.deck)

    def show_deck(self):
        for i_card in self.deck:
            i_card.info()
        print('Всего {} карт.'.format(len(self.deck)))

    def get_card(self):
        return self.deck.pop(0)


class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
        self.score = 0

    def add_card(self, card):
        self.cards.append(card)
        self.score += card.get_price()
        if card.name == 'Ace' and self.score > 21:
            self.score -= 10

    def get_score(self):
        return self.score

    def info(self):
        print('Имя игрока:     {},\nНабрано очков:  {}'.format(
            self.name,
            self.score
        ))
        print('Карты на руках:')
        for i_card in self.cards:
            i_card.info()
        print()
