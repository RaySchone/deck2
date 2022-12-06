import random


# this creates the class so our cards can have a value added to them
class Value:
    pass


# this creates the ability to assign a suit to the cards
class Suit:
    pass


# this creates the cards themselves and changes 1, 11, 12, and 13 to their respective letters
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


# this sets up the deck and gives the ability to randomizes/shuffle the deck
class Deck:
    def __init__(self):
        self.cards = []

    def shuffle_deck(self):
        random.shuffle(self.cards)

    # this gives the suits a symbol of heart spade club and diamonds instead of a letter
    # it also sets the limit of the cards from 1-13 for each suit
    def create_deck(self):
        for suit in ["\u2665", "\u2666", "\u2663", "\u2660"]:
            for value in range(1, 14):
                new_card = Card(value, suit)
                self.cards.append(new_card)

    # this makes the cards
    def print_deck(self):
        for card in self.cards:
            print(card.cardValue, card.cardSuit)

    # this pulls a card from the deck
    def get_card(self):
        for card in self.cards:
            print(card)

# hi
# the calls to action
new_deck = Deck()
new_deck.create_deck()
new_deck.shuffle_deck()
new_deck.print_deck()
#new_deck.get_card()
