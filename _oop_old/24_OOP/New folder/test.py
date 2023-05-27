values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]


def test_fnc(v, s):
    i = 0
    deck = []
    while i < len(suits):
        j = 0
        while j < len(values):
            card = []
            card.append(suits[i])
            card.append(values[j])
            # print(card)
            deck.append(card)
            card = []
            # print(deck)
            j += 1
        i += 1
        # while j < len(values)
    return len(deck)


print(test_fnc(values, suits))
