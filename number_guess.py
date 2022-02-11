import random

random_number = random.randint(0, 50)
user_input = input("Enter the number: ")
if user_input.isdigit():
    user_input = int(user_input)
    if user_input <=0:
        print("Please, next time enter the number > than 0")
        quit()
else:
    print("Your input is not the number, Please next time type the number...")
    quit()

guess_score = 0

while True:
    guess_score +=1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please, type a number!")
        continue
    if user_guess == random_number:
        print(f"Your guess number {user_guess} is = random number {random_number}")
        break
    elif user_guess < random_number:
        print("Your input is too low, Input larger number!")
    elif user_guess > random_number:
        print("Your input is too high, Input lower number!")
print(f"You got it in {guess_score} guesses")