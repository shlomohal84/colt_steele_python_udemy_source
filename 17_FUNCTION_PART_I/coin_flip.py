from random import random


def flip_coin():
    if random() > 0.5:
        return "Heads"
    else:
        return "Tails"


result = flip_coin()
print(result)
