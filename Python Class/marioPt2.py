#rock = 1 paper = 2 sccisors = 3
game = input("Do you want to play rock, paper, or scissors? Type Y or N.")
while game == "Y" or game == "y":
    user = input("rock, paper, or scissors?")
    print (user)
    while user != "rock" and user != "paper" and user != "scissors":
        print("You can only choose rock, paper, or scissors!")
        user = input("rock, paper, or scissors?")
        print(user)
    from random import *
    computer_stuff = randint(1,3)
    print (computer_stuff)
    if computer_stuff == 1 and user == "rock":
        print("You tied. Computer chose rock")
    elif computer_stuff == 2 and user == "rock":
        print("You lose. Computer chose paper")
    elif computer_stuff == 3 and user == "rock":
        print("You Win! Computer chose scissors")
    if computer_stuff == 1 and user == "paper":
        print("You win! Computer chose rock")
    elif computer_stuff == 2 and user == "paper":
        print("You tied. Computer chose paper") 
    elif computer_stuff == 3 and user == "paper":
        print("You lose computer chose scissors") 
    if computer_stuff == 1 and user == "scissors":
        print("You lose. Computer chose rock")
    elif computer_stuff == 2 and user == "scissors":
        print("You win! Computer chose paper")
    elif computer_stuff == 3 and user == "scissors":
        print("You tied. Computer chose scissors")
    game = input("Do you want to play rock, paper, or scissors? Type Y or N.")
