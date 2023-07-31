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
        self.cards = [[x, y] for x in self.suit_lst for y in self.value_lst]

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    def _deal(self, num=1):
        if num != int(num) or num <= 0:
            raise ValueError(f"Invalid value")

        elif num > len(self.cards):
            raise ValueError(
                f"Value {num} is bigger than deck's size of {len(self.cards)}"
            )
        elif len(self.cards) == 0:
            raise ValueError(f"All cards have been dealt")

        elif num == 1:
            return self.cards.pop()
        hand = self.cards[-1 : -num - 1 : -1]
        self.cards = self.cards[:-num]
        return hand

    def count(self):
        return f"{len(self.cards)}"

    def deal_card(self):
        return self._deal()

    def deal_hand(self, num):
        return self._deal(num)


deck = Deck()
# print(deck.cards)
# print(deck.deal_card())
print(deck.deal_hand(5))
# print(len(deck.cards))
