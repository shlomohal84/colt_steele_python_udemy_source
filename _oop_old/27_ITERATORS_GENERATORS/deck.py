from random import shuffle


class Card:
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)


class Deck:
    def __init__(self):
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.cards = [Card(value, suit) for value in values for suit in suits]

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, amount):
        count = self.count()
        actual_deal = min([count, amount])
        if count == 0:
            raise ValueError("All cards have been dealt")
        cards = self.cards[-actual_deal:]
        self.cards = self.cards[:-actual_deal]
        return cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self.cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, amount):
        return self._deal(amount)


# d = Deck()
# print(d.shuffle())
# print(d.cards)

my_deck = Deck()
my_deck.shuffle()

for card in my_deck:
    print(card)
