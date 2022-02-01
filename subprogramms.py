import random
import csv

# Subprogramms challenges

# def number():
#     num = int(input("Enter number: "))
#     return num
# def count_num(num):
#     for i in range(1,num+1):
#         print(i)
# def main():
#     num = number()
#     count_num(num)
# main()

# def number():
#     low_num = int(input("Enter low number: "))
#     high_num = int(input("Enter high number: "))
#     comp_num = random.randint(low_num, high_num)
#     return comp_num
# def instruction():
#     print("I am thinking of a number...\n")
#     guess_number = int(input("Guess the number: "))
#     return guess_number
# def checking(comp_num, guess_number):
#     againTry = True
#     while againTry == True:
#         if comp_num == guess_number:
#             print("Correct, you win!")
#             againTry = False
#         elif comp_num > guess_number:
#             print("Too low")
#             guess_number = int(input("Guess the number: "))
#         elif comp_num < guess_number:
#             print("Too high")
#             guess_number = int(input("Guess the number: "))
   
# def main():
#     comp_num = number()
#     guess_number = instruction()
#     checking(comp_num, guess_number)
# main()

# def add():
#     num1 = random.randint(5,20)
#     num2 = random.randint(5,20)
#     display = str(num1) + "+" + str(num2) + "= "
#     answer = int(input(display))
#     real_answer = num1 + num2
#     combined = (answer, real_answer)
#     return combined

# def substraction():
#     num1 = random.randint(25,50)
#     num2 = random.randint(1,25)
#     display = str(num1) + "-" + str(num2) + "= "
#     answer = int(input(display))
#     real_answer = num1 - num2
#     combined = (answer, real_answer)
#     return combined

# def check(answer, real_answer):
#     if answer == real_answer:
#         print("Correct")
#     else:
#         print("Incorrect, The answer is ", real_answer)

# def main():
#     print("1)Addition\n2)Substraction\n")
#     menu = int(input("Enter 1 or 2: "))
#     if menu == 1:
#         answer, real_answer = add()
#         check(answer, real_answer)
#     elif menu == 2:
#         answer, real_answer = substraction()
#         check(answer, real_answer)
#     else:
#         print("Not valid selection!")
# main()

# list = []
# def add():
#     name = input("Enter the name to add into the list: ")
#     list.append(name)
#     return list
# def change():
#     for i in list:
#         print(i)
#     selected_number = int(input("Enter the number of the name to be changed: "))
#     name = input("Enter the name to be changed: ")
#     list[selected_number] = name
# def delete():
#     name = int(input("Enter the name index to be deleted from the list: "))
#     del list[name]
#     return list
# def view_all():
#     for name in list:
#         print(name)

# def main():
#     again = "yes"
#     while again == "yes":
#         print("1)Add a name to the list\n2)Change name from the list\n3)Delete a name from the list\n4)View all the names from the list\n5)Quit")
#         menu = int(input("Enter 1 or 2 or 3 or 4 or 5: "))
#         if menu == 1:
#             name = add()
#         elif menu == 2:
#             name = change()
#         elif menu == 3:
#             name = delete()
#         elif menu == 4:
#             name = view_all()
#         elif menu == 5:
#             again = "no"
#         else:
#             print("Incorrect input!")
#         data = (list, again)
    
# main()

# def add():
#     file = open("Salaries.csv", "a")
#     name = input("Enter your name: ")
#     salary = int(input("Enter your salary in $: "))
#     newRecord = name + ", " + str(salary) + "\n"
#     file.write(newRecord)
#     file.close()

# def display():
#     file = open("Salaries.csv", "r")
#     for i in file:
#         print(i)
#     file.close()

# def main():
#     print("1)Add to a file\n2)View all record\n3)Quit program")
#     again = "yes"
#     while again == "yes":
#         menu = int(input("Enter 1 2 or 3: "))
#         if menu == 1:
#             add()
#         elif menu == 2:
#             display()
#         elif menu == 3:
#             again = "no"
#         else:
#             print("Incorrect option")
# main()
            
# def add():
#     file = open("Salaries.csv", "a")
#     name = input("Enter your name: ")
#     salary = int(input("Enter your salary in $: "))
#     newRecord = name + ", " + str(salary) + "\n"
#     file.write(newRecord)
#     file.close()

# def display():
#     file = open("Salaries.csv", "r")
#     for i in file:
#         print(i)
#     file.close()

# def delete():
#     x = 0
#     file = list(csv.reader(open("Salaries.csv")))
#     tmp = []
#     for row in file:
#         tmp.append(row)
#         display = x, tmp[x]
#         print(display)
#         x +=1
#     remove_row = int(input("Which row you want to delete from the list: "))
#     del tmp[remove_row]

#     for i in tmp:
#         print(i)
#     file = open("Salaries.csv", "w")
#     x = 0
#     for row in tmp:
#         newRecord = tmp[x][0] + "," + tmp[x][1] + "\n"
#         file.write(newRecord)
#         x+=1
#     file.close()

# def main():
#     print("1)Add to a file\n2)View all record\n3)Delete a record\n4)Quit program")
#     again = "yes"
#     while again == "yes":
#         menu = int(input("Enter 1 2 3 or 4: "))
#         if menu == 1:
#             add()
#         elif menu == 2:
#             display()
#         elif menu == 3:
#             delete()
#         elif menu == 4:
#             again = "no"
#         else:
#             print("Incorrect option")
# main()
  
