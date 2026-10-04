import random 
choices = ["rock", "paper", "scissors"]
print("rock crushes scissors, scissors cuts paper, paper covers rock")

while True:
    player = input("do you want to be rock, scissors, paper (or quit)? ")
 
    if player not in choices:
        print("invalid choice, please choose rock, paper, or scissors.")
    if player == "quit":
        print("you quit the game.")
        break
    if player == "rock":
        print("it's a tie!")
        continue
    if player == ("paper"):
        print("it's a tie!") 
        continue   
    elif player == ("scissors"):
        print("you lose!") 
        continue
else:
    print("you win!") 
