# Reading and Writing to a Text File

# file = open("Countries.txt", "w")
# file.write("Italy\n")
# file.write("Canada\n")
# file.write("USA\n")
# file.close()

# file = open("Countries.txt", "r")
# print(file.read())

# file = open("Countries.txt", "a")
# file.write("Franse\n")
# file.close()

# file = open("Countries.txt", "r")
# print(file.read())

# challenges

# file = open("Numbers.txt", "w")
# file.write("1, ")
# file.write("2, ")
# file.write("3, ")
# file.write("4, ")
# file.write("5 ")
# file.close()

# file = open("Names.txt", "w")
# file.write("Alex\n")
# file.write("Anna\n")
# file.write("Bob\n")
# file.write("Tom\n")
# file.write("Jack\n")
# file.close()

# file = open("Names.txt", "r")
# print(file.read())

# file = open("Names.txt", "a")
# new_name = input("Enter new name: ")
# file.write(new_name + "\n")
# file.close()
# file = open("Names.txt", "r")
# print(file.read())

# print(" 1)Create a new file\n 2)Display the file\n 3)Add a new item to the file\n Make a selection 1, 2, or 3: ")
# select_menu = int(input(" Enter 1, 2 or 3: "))
# if select_menu!=1 and select_menu!=2 and select_menu!=3:
#     print("Error, choose only 1, 2 or 3")
# elif select_menu == 1:
#     subject = input(" Enter a school subject: ")
#     file = open("Subject.txt", "w")
#     file.write(subject + "\n")
#     file.close()
# elif select_menu == 2:
#     file = open("Subject.txt", "r")
#     print(file.read())
# elif select_menu == 3:
#     new_subject = input(" Enter a new subject: ")
#     file = open("Subject.txt", "a")
#     file.write(new_subject + "\n")
#     file.close()

# file = open("Names.txt", "r")
# print(file.read())
# file = open("Names.txt", "r")
# name = input("Enter the name from the list: ")
# name = name + "\n"
# for i in file:
#     if i != name:
#         file = open("Names2.txt", "a")
#         newrecord = i
#         file.write(newrecord)
#         file.close()
# file.close()    