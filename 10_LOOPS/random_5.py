# use randint(a, b) to generate a random number between a and b
from random import randint

number = 0  # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:
    i += 1
    number = randint(1, 10)
    print(f"Attempt #{i} - rolled: {number}")
