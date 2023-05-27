# Rock, Paper, Scissors Mini-Game
# Version 1

r = "rock"
p = "paper"
s = "scissors"

player1 = input("Player #1 make your move: ")
player2 = input("Player #2 make your move: ")

if (player1 == player2):
    print("Draw!")
elif (player1 == r and player2 == s) or (player1 == p and player2 == r) or (player1 == s and player2 == p):
    print("Player #1 wins!")
else:
    print("Player #2 wins!")
