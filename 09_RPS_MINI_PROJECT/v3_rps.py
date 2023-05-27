# Rock, Paper, Scissors Mini-Game
# Version 3 - Vs CPU


from random import randint

r = "rock"
p = "paper"
s = "scissors"
print(f"...{r}...\n...{p}...\n...{s}...")
opts = [r, p, s]


player1 = input("Player #1 make your move: ").lower()
# print("*** NO CHEATING!\n" * 20)
cpu = opts[randint(0, 2)]
# cpu = random.choice(opts)
print('CPU\'s move: ' + cpu)

if (player1 == cpu):
    print("Draw!")
elif player1 == r:  # Rock
    if cpu == p:
        print("CPU wins!")
    else:
        print("Player #1 wins!")
elif player1 == p:  # Paper
    if cpu == r:
        print("Player #1 wins!")
    else:
        print("CPU wins!")
elif player1 == s:  # Scissors
    if cpu == r:
        print("CPU wins!")
    else:
        print("Player #1 wins!")


else:
    print("Invalid parameters")
# elif (player1 == r and player2 == s) or (player1 == p and player2 == r) or (player1 == s and player2 == p):
#     print("Player #1 wins!")
# else:
#     print("CPU wins!")
