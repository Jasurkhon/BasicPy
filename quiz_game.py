import random
print("*** Welcome to the quiz game ***")
choice = input("Do you wanna play game? y/n ")
if choice.lower() == "y":
    print("Well, Let's play game!")
    score = 0

    number1 = random.randint(1,50)
    number2 = random.randint(1,50)
    user_answer = int(input((str(number1) + "+" + str(number2) + " = ")))
    real_answer = number1 + number2
    if user_answer == real_answer:
        print("Correct!")
        score += 1
    elif user_answer != real_answer:
        print("Incorrect answer!")
    
    number1 = random.randint(1,50)
    number2 = random.randint(1,50)
    user_answer = int(input((str(number1) + "-" + str(number2) + " = ")))
    real_answer = number1 - number2
    if user_answer == real_answer:
        print("Correct!")
        score += 1
    elif user_answer != real_answer:
        print("Incorrect answer!")
    
    number1 = random.randint(1,50)
    number2 = random.randint(1,50)
    user_answer = int(input((str(number1) + "*" + str(number2) + " = ")))
    real_answer = number1 * number2
    if user_answer == real_answer:
        print("Correct!")
        score += 1
    elif user_answer != real_answer:
        print("Incorrect answer!")
    
    number1 = random.randint(1,50)
    number2 = random.randint(1,50)
    user_answer = int(input((str(number1) + "//" + str(number2) + " = ")))
    real_answer = number1 // number2
    if user_answer == real_answer:
        print("Correct!")
        score += 1
    elif user_answer != real_answer:
        print("Incorrect answer!")
else:
    quit()

print(f"You got {score} right answers!")
print(f"You got {(score/4)*100} %")