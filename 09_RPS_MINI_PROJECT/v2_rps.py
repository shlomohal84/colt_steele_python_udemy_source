# Rock, Paper, Scissors Mini-Game
# Version 2

r = "rock"
p = "paper"
s = "scissors"

player1 = input("Player #1 make your move: ")
print("*** NO CHEATING!\n" * 20)
player2 = input("Player #2 make your move: ")

if (player1 == player2):
    print("Draw!")
elif player1 == r:  # Rock
    if player2 == p:
        print("Player #2 wins!")
    elif player2 == s:
        print("Player #1 wins!")
elif player1 == p:  # Paper
    if player2 == r:
        print("Player #1 wins!")
    elif player2 == s:
        print("Player #2 wins!")
elif player1 == s:
    if player2 == r:
        print("Player #2 wins!")
    elif player2 == p:
        print("Player #1 wins!")


else:
    print("Invalid parameters")
# elif (player1 == r and player2 == s) or (player1 == p and player2 == r) or (player1 == s and player2 == p):
#     print("Player #1 wins!")
# else:
#     print("Player #2 wins!")
