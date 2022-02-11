name = input("Enter your name, before starting to play the game: ")
print(f"Welcome {name} to this adventure!")
answer = input("You were walking in this road, but now you are in the end of it. You can go to right or left. Please type <left> to go to left or <right> to go to right: ")
if answer.lower() == "left":
    answer = input("You come to the river. You have 2 options: you can 'walk' around it or 'swim': ")
    if answer.lower() == "walk":
        print("You walked for long distance and you are out of the map. You lost the game. Thanks for participation")
    elif answer.lower() == "swim":
        print("You swam across the river and as the result you were eaten by alligator.")
    else:
        print("Invalid option! Thanks for playing")
elif answer.lower() == "right":
    answer = input("You come to the bridge and you have options to 'cross it' or 'go back': ").lower()
    if answer == "cross":
        answer = input("You crossed the beidge and met the person. Would you like to tell with him 'yes' or 'no': ").lower()
        if answer == "yes":
            print("You choose right option. Congratulations you WIN!!!!")
        elif answer == "no":
            print("You loose the game")
        else:
            print("Invalid option! Thanks for playing")    
    elif answer == "go back":
        print("You choose 'back' option and loose the game!")
    else:
        print("Invalid option! Thanks for playing")    
else:
    print("Invalid option! Thanks for playing")