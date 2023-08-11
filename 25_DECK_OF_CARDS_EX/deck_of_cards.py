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
        self.cards = [Card(x, y)
                      for x in self.suit_lst for y in self.value_lst]

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    def _deal(self, num=1):
        if num != int(num) or num <= 0:
            raise ValueError(f"Invalid value")
        elif len(self.cards) == 0:
            raise ValueError(f"All cards have been dealt")
        elif num == 1:
            return self.cards.pop()
        hand = self.cards[-1: -num - 1: -1]
        self.cards = self.cards[:-num]
        return hand[::-1]

    def shuffle(self):
        if len(self.cards) < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)

    def count(self):
        return len(self.cards)

    def deal_card(self):
        return self._deal()

    def deal_hand(self, num):
        return self._deal(num)


deck = Deck()
print(deck)

print(deck.count())
# print(deck.shuffle())

# print(deck.deal_card())
print(deck.deal_hand(100))
# print(len(deck.cards))
# print(deck)
# print(deck.shuffle())
