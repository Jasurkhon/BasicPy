# more string manipulation challenges

# fname = input("Enter your firstname: ")
# print("Length of your firstname =", fname, ":",len(fname))
# sname = input("Enter your surname: ")
# print("Length of your surname =", sname, ":",len(sname))
# total_name = fname + " " + sname
# print("Full name: ", total_name)
# print("Length of your full name (", total_name,") = ",len(total_name))


# subject = input("Enter your favourite subject: ")
# for i in subject:
#     print(i, end="-")

# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"
# spoint = int(input("Enter starting point: "))
# epoint = int(input("Enter ending point: "))
# print("Characters between", spoint, "and", epoint, text[spoint:epoint])

# word = input("Enter the word in uppercase: ")
# tryAgain = False
# while tryAgain == False:    
#     if word.isupper():
#         print("Well done, word in uppercase")
#         tryAgain = True
#     else:
#         print("Try again")
#         word = input("Enter the word in uppercase: ")

# postcode = input("Enter your postcode: ")
# print(postcode[0:2].upper())

# name = input("Enter your name: ")
# count = 0
# for l in name:
#     if l =="a" or l == "e" or l == "i" or l == "o" or l == "u":
#         count = count + 1
# print("There are ", count, "vowels in your name")

# npassword = input("Enter new password: ")
# apassword = input("Enter password again: ")
# if npassword == apassword:
#     print("Thank you")
# elif npassword.lower() == apassword.lower():
#     print("They must be in same case")
# else:
#     print("Incorrect")

# word = input("Enter the word: ")
# count = 1
# for i in word:
#     position = len(word) - count
#     print(word[position])
#     count = count + 1