#import randit from random
from random import randint

#list of options
#list of variables
p = ["rock", "paper", "scissors"]

#set a random player
#random number variable
computer = p[randint(0,2)]

#set player to false
#boolean variable
player = False

while player == False:
#set player to true
    player = input("rock, paper or scissors?")
#if player picks same value as computer = tie
    if player == computer:
        print("tie! Play again.")
#if player picks rock and computer picks paper you lose
    elif player == "rock":
        if computer == "paper":
            print("you lose! Try again, best of 3.")
#else you win
        else:
            print("you win!")
#if player picks paper and computer picks rock you win
    elif player == "paper":
       if computer == "rock":
            print("you win!")
        # else you win
       else:
            print("you lose!")
#else if player pickcs scissors and computer picks rock you lose
    elif player == "scissors":
        if computer == "rock":
            print("you lose! Try again, best of 3.")
#else you win
        else:
            print("you win!")
#if player makes a mistake or error, else anothing other than the options are answered
    else:
        print("pick a valid answer, all lower-case please.")
    #reset player to false
    player = False
    computer = p[randint(0,2)]

#Ehsan Rajabi
