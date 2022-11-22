import random


class Value:
    pass


class Suit:
    pass


class Card:
    def __init__(self, value, suit):
        self.cardValue = value
        self.cardSuit = suit
        if value == 1:
            self.cardValue = "A"
        elif value == 11:
            self.cardValue = "J"
        elif value == 12:
            self.cardValue = "Q"
        elif value == 13:
            self.cardValue = "K"


class Deck:
    def __init__(self):
        self.cards = []

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def create_deck(self):
        for suit in ["\u2665", "\u2666", "\u2663", "\u2660"]:
            for value in range(1, 14):
                new_card = Card(value, suit)
                self.cards.append(new_card)

    def print_deck(self):
        for card in self.cards:
            print(card.cardValue, card.cardSuit)

    def get_card(self):
        pass


new_deck = Deck()
new_deck.create_deck()
new_deck.shuffle_deck()
new_deck.print_deck()
