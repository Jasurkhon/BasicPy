# for loop
 
# name = input("Enter your name: ")
# for i in range(0,3):
#      print(name)

# name = input("Enter your name: ")
# num = int(input("Enter number: "))
# for i in range(1, num):
#     print(i, name)

# name = input("Enter your name: ")
# for i in name:
#     print(i)

# name = input("Enter your name: ")
# num = int(input("Enter num: "))
# for i in name:
#     for x in range(num):
#         print(i)

# num = int(input("Enter number between 1 and 12: "))
# for i in range(num,num*11, num):
#     print(i)

# num = int(input("Enter number between 1 and 12: "))
# for i in range(1, 13):
#     answer = i *num
#     print(i, "*", num, "=", answer) 

# num = int(input("Enter num below 50: "))
# print("You entered:", num)
# for i in range(50, num-1, -1):
#     print(i)

# name = input("Enter your name: ")
# num = int(input("Enter the num: "))
# if num < 10:
#     for x in range(0, num):
#         print(name)
# else:
#     for i in range(0, 3):
#         print("Too high!!!")

# total = 0
# for i in range(0, 5):
#     num = int(input("Enter 5 different numbers: "))
#     answer = input("Do you want that number to be included???")
#     if answer.lower() == "yes":
#         total = total + num
#     else:
#         total = total
# print("Total = ", total)

# answer = input("Which direction you want to count\n1)UP\n2)DOWN\n ")
# if answer.lower() == "up":
#     top = int(input("Enter top value: "))
#     for i in range(1, top+1, 1):
#         print(i)
# elif answer.lower() == "down":
#     down = int(input("Enter the num below 20: "))
#     for i in range(20, down-1, -1):
#         print(i)
# else:
#     print("I don'n understand(")

# num = int(input("How many people you want to invive to a party???: "))
# if num < 10:
#     for i in range(0, num):
#         name = input("Enter the name: ")
#         print(name, "has been invited to a party")
# elif num >= 10:
#     print("Too many people!")