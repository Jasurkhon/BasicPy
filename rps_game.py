#  rock, paper, scissor game

import random

user_score = 0
comput_score = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter rock/paper/scissors or Q for quit: ")
    if user_input.lower() == "q":
        break
    if user_input not in options:
        continue
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print(f"Computer picked { computer_pick } option.")
    
    if user_input == "rock" and computer_pick == "scissors":
        print("You win")
        user_score +=1
    elif user_input == "scissors" and computer_pick == "paper":
        print("You win")
        user_score +=1
    elif user_input == "paper" and computer_pick == "rock":
        print("You win")
        user_score +=1
    else:
        print("Computer win")
        comput_score +=1 
print(f"You won {user_score} times")
print(f"Computer won {comput_score} times")
print("Thanks for playing :)")