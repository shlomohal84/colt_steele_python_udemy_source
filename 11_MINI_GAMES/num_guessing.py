from random import randint


guess = None

num = randint(1, 10)

while True:
    guess = input("Guess the number (1-10): ")
    guess = int(guess)
    while num != guess:
        guess = int(guess)
        if guess > 10 or guess < 1:
            guess = input("Out of range. Try again (1-10)")
        elif guess < num:
            guess = input("Too low. Try again: ")
        elif guess > num:
            guess = input("Too high. Try again: ")

    print(f"Correct! Rolled number was {num}")
    game_status = input("Would you like to play again? (y/n)")
    if game_status == "Y" or game_status == "y":
        guess = None
        num = randint(1, 10)
    else:
        print("Bye! Have a nice day!")
        break
