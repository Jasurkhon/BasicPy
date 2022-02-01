import csv
import random
from tkinter.messagebox import QUESTION

# file = open("Stars.csv", "w")
# newRecord = "Brian, 73, Taurus\n"
# file.write(str(newRecord))
# file.close()

# file = open("Personal.csv", "w")
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# newRecord = name + ", " + age + "\n"
# file.write(str(newRecord))
# file.close()

# file = open("Personal.csv", "r")
# for i in file:
#     print(i)

# file = open("Personal.csv", "r")
# reader = csv.reader(file)
# rows = list(reader)
# print(rows[0])

# file = open("Stars.csv", "r")
# search = input("Enter the data that you are searching: ")
# reader = csv.reader(file)
# tryAgain = True
# while tryAgain == True:
#     for row in file:
#         if search in str(row):
#             print(row)
#             tryAgain = False
#         else:
#             print("No info!!!")
#             search = input("Try again: ")
#             file = open("Stars.csv", "r")
            
# file = list(csv.reader(open("Stars.csv")))
# tmp = []
# for row in file:
#     tmp.append(row)

# file = open("NewStars.csv", "w")
# x = 0
# for row in tmp:
#     newRec = tmp[x][0] + "," + tmp[x][1] + "," + tmp[x][2] + "\n"
#     file.write(newRec)
#     x = x + 1
# file.close()

# challenges

# file = open("Books.csv", "w")
# newRecord = "To Kill A Mockingbird, Harper Lee, 1960\n"
# file.write(newRecord)
# newRecord = "A Brief History of Time, Stephen Hawking, 1988\n"
# file.write(newRecord)
# newRecord = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
# file.write(newRecord)
# newRecord = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
# file.write(newRecord)
# newRecord = "Pride and Prejudice, Jane Austen, 1813\n"
# file.write(newRecord)

# file = open("Books.csv", "a")
# newRecord = input("Enter another record: ")
# file.write(newRecord + "\n")
# file = open("Books.csv", "r")
# for row in file:
#     print(row)

# number_record = int(input("How many records you want to add: "))
# file = open("Books.csv", "a")
# for i in range(number_record ):
#     title = input("Enter title of the book: ")
#     author = input("Enter author of the book: ")
#     year = input("Enter the year it was realised: ")
#     newRecord = title + "," + author + "," + year + "\n"
#     file.write(str(newRecord))
# file.close() 
# search_author = input("Enter author of the books to be displayed: ")
# file = open("Books.csv", "r")
# count = 0
# for row in file:
#     if search_author in str(row):
#         print(row)
#         count = count + 1
# if count == 0:
#     print("Given author is not in the list!")
# file.close()

# start_year = int(input("Enter starting year: "))
# end_year = int(input("Enter ending year: "))
# file = list(csv.reader(open("Books.csv")))
# tmp = []
# for row in file:
#     tmp.append(row)
# x = 0
# for row in tmp:
#     if int(tmp[x][2]) >= start_year and int(tmp[x][2]) <= end_year:
#         print(tmp[x])
#     x = x + 1

# file = list(csv.reader(open("Books.csv")))
# tmp = []
# for row in file:
#     tmp.append(row)
# count = 0
# for row in tmp:
#     print(count, row)
#     count = count + 1

# file = list(csv.reader(open("Books.csv")))
# tmp = []
# for row in file:
#     tmp.append(row)
# for i in tmp:
#     print(i)
# remove_row = int(input("Which row you want to delete from the list: "))
# del tmp[remove_row]
# for i in tmp:
#     print(i)
# change_data = int(input("Which row of data you want to change: "))
# count = 0
# for row in tmp[change_data]:
#     display = count,tmp[change_data][count]
#     print(display)
#     count = count + 1
# part_change = int(input("Which part do you want to change: "))
# newData = input("Enter new Data: ") 
# tmp[change_data][part_change] = newData
# print(tmp[change_data])
# file = open("Books.csv", "w")
# count = 0
# for row in tmp:
#     newRecord = tmp[count][0] + "," + tmp[count][1] + "," + tmp[count][2] + "\n"
#     file.write(newRecord)
#     count = count + 1
# file.close()

# score = 0
# name = input("Enter your name: ")
# q1_num1 = random.randint(10,50)
# q1_num2 = random.randint(10,50)
# question1 = str(q1_num1) + "+" + str(q1_num2) + "="
# input_answer1 = int(input(question1))
# answer1 = q1_num1 + q1_num2
# if input_answer1 == answer1:
#     score = score + 1
# q2_num1 = random.randint(10,50)
# q2_num2 = random.randint(10,50)
# question2 = str(q2_num1) + "-" + str(q2_num2) + "="
# input_answer2 = int(input(question2))
# answer2 = q2_num1 - q2_num2
# if input_answer2 == answer2:
#     score = score + 1
# file = open("Quiz.csv", "a")
# newRecord = name + " " + question1 + str(answer1) + " " + question2 + str(answer2) + " " + str(score) + " " + "\n"
# file.write(newRecord)
# file.close()