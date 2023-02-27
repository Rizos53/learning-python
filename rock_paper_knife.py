rock = "rock".lower()
paper = "paper".lower()
knife = "knife".lower()
status_true = True

print("This is the rock, paper, knife game. If you want to quit, enter: Quit or q ")
while status_true:
    player1 = input("(player1) rock, paper or knife? ")
    if player1.lower() == "quit" or player1.lower() == "q":
        break
    player2 = input("(player2) rock, paper or knife? ")
    if player2.lower() == "quit" or player2.lower() == "q":
        break
    elif player1 == player2:
        print("Tie!")
    elif player1 == rock and player2 == knife:
        print("Rock beats knife, (Player1) has won!")
    elif player1 == paper and player2 == rock:
        print("Paper beats rock, (Player1) has won!")
    elif player1 == knife and player2 == paper:
        print("knife beats paper, (Player1) has won!")
    elif player2 == rock and player1 == knife:
        print("Rock beats knife, (Player2) has won!")
    elif player2 == paper and player1 == rock:
        print("Paper beats rock, (Player2) has won!")
    elif player2 == knife and player1 == paper:
        print("Knife beats paper, (player2) has won!")
    elif player1 or player2 not in ["rock", "paper", "knife"]:
        print("Input is invalid. Please choose the following options: Rock, Paper, Knife")




