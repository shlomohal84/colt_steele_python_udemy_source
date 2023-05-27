# Rock, Paper, Scissors Mini-Game
# Version 3 - Vs CPU


from random import randint

r = "rock"
p = "paper"
s = "scissors"
print(f"...{r}...\n...{p}...\n...{s}...\nBest out of seven!")
opts = [r, p, s]

winning_score = 4
player_wins = 0
cpu_wins = 0

while player_wins < winning_score and cpu_wins < winning_score:
    # print('***********')
    # print(f"Score is: Player1 {player_wins} - {cpu_wins} CPU")
    player1 = input("(Player #1 make your move): ").lower()

    if player1.lower() == "quit" or player1.lower() == "q":
        print("\nAdiós!")
        break
    if player1 != r and player1 != p and player1 != s:
        print("Invalid parameters")
    else:
        cpu = opts[randint(0, 2)]
        print('CPU\'s move: ' + cpu)
        if (player1 == cpu):
            print("Draw!")
        elif player1 == r:  # Rock
            if cpu == p:
                print("CPU wins!")
                cpu_wins += 1
            else:
                print("Player #1 wins!")
                player_wins += 1
        elif player1 == p:  # Paper
            if cpu == r:
                print("Player #1 wins!")
                player_wins += 1
            else:
                print("CPU wins!")
                cpu_wins += 1
        elif player1 == s:  # Scissors
            if cpu == r:
                print("CPU wins!")
                cpu_wins += 1
            else:
                print("Player #1 wins!")
                player_wins += 1
        print('\n***********')
        print(f"Score is: Player1 {player_wins} - {cpu_wins} CPU")

if player_wins == winning_score or cpu_wins == winning_score:
    if player_wins > cpu_wins:
        print('game over! player #1 wins!'.upper())

    elif player_wins < cpu_wins:
        print('game over! cpu wins!'.upper())


# elif (player1 == r and player2 == s) or (player1 == p and player2 == r) or (player1 == s and player2 == p):
#     print("Player #1 wins!")
# else:
#     print("CPU wins!")
