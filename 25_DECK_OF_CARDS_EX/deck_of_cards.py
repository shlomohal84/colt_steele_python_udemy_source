from random import choice, shuffle


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.suit_lst = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.value_lst = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K",
        ]
        self.cards = [Card(x, y) for x in self.suit_lst for y in self.value_lst]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()

        actual = min([count, num])
        if count == 0:
            raise ValueError("All cards have been dealt")
        hand = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return hand

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)


deck = Deck()
# print(deck)

# print(deck.shuffle())

# print(deck.deal_card())
print(deck.deal_hand(55))
print(deck.count())
# print(deck.deal_hand(3))
# print(deck.deal_hand(3))
# print(deck.deal_hand(3))
# print(deck.deal_hand(3))

# print(deck.deal_card())
# print(deck)
# print(deck.shuffle())
