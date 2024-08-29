player1 = input()
player2 = input()

rules = {
    "rock" : "scissors",
    "scissors" : "paper",
    "paper" : "rock"
}

if player1 == player2:
    print("Draw")
elif rules[player1] == player2:
    print("Player 1")
else:
    print("Player 2")