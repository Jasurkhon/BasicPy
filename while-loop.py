#  while loop

# total = 0
# while total <= 50:
#     num = int(input("Enter the num: "))
#     total = total + num
#     print("The total is", total)

# num = 0
# while num <5:
#     num = int(input("Enter the num: "))
# print("The last num you entered was a ", num)

# num1 = int(input("Enter num1: "))
# total = num1
# answer = "y"
# while answer =="y":
#     num2 = int(input("Enter num2: "))
#     answer = input("Do you want to add another number??? (y or n)")
#     total = total + num2
# print("Total = ", total)

# count = 0
# answer ="y"
# while answer == "y":
#     name = input("Enter the name of person who you want to invite to the party: ")
#     print(name, "has been invited to the party")
#     count = count+1
#     answer = input("Do you want to invite somebody else? ")
# print(count, "people are coming to the party")

# compnum = 50
# count = 1
# num = int(input("Enter the value of num: "))
# while num !=compnum:
#     if num < compnum:
#         print("Too low!")
#     else:
#         print("Too high!")
#     count = count+1
#     num = int(input("Have another guess: "))
# print("Well done, you took", count, "attempts")

# num = int(input("Enter number between 10 and 20: "))
# while num <10 or num > 20:
#     if num < 10:
#         print("Too low!")
#     else:
#         print("Too high!")
#     num = int(input("Try again: "))
# print("Thank you!")

# num = 10
# while num > 0:
#     print("There are", num, "green bottles hanging on the wall")
#     print(num, "green bottles hanging on the wall, and if 1 green bottle should accidently fall")
#     num = num-1
#     answer= int(input("How many green bottles will be hanging on the wall?: "))
#     if answer == num:
#         print("There will be", num, "green bottles hanging on the wall")
#     else:
#         while answer!=num:
#             answer = int(input("No, try again: "))
# print("There are no more green bottles hanging on the wall")
