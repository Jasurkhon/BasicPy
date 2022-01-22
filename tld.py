# Tuples, lists and dictionaries challenges
# tuple () content can't be changed while program runs
# list [] content can be changed while program runs
# dictionary{1:"smth", 2:"smth"}

# fruit_tuple = ("banana", "orange", "cherry")
# print("The index of banana: ", fruit_tuple.index("banana"))

# name_list = ["John", "Alex", "Mike"]
# # delete name from list 
# del name_list[1]
# print(name_list)
# # add new name in the end
# name_list.append(input("Enter new name: ")) 
# print(name_list)
# # sorts list in alphabetical order in the new order. Doen't work if items of differen types
# name_list.sort()
# print(name_list)

# color = {1:"red", 2:"blue", 3:"yellow"}
# print("Before:", color[2])
# color[2] = "yellow"
# print("After: ", color[2])


num = [1,2,3,4,5,6,7,8,9,10]
# print("There are:", len(num), "items")
# print(num[1:11])
# for i in num:
#     print(i)

# num1 = int(input("Enter num: "))
# if num1 in num:
#     print(num1, "in the list")
# else:
#     print(num1, "is not in the list")

# num.insert(0,5) insert 5 at index 0
# print(num)
# num.remove(0) remove 0 from the list
# print(num)
# num.append(15) adds 15 to the end of the list
# print(num)

# challenges

# country = ("Albania", "Australia", "Belgium", "Brazil", "Canada")
# print(country)
# country_pick = input("Enter county from the given tuple: ")
# print("Index of that country:", country.index(country_pick.capitalize()))


# country = ("Albania", "Australia", "Belgium", "Brazil", "Canada")
# print(country)
# country_pick = input("Enter county from the given tuple: ")
# print("Index of that country:", country.index(country_pick.capitalize()))
# num = int(input("Enter num: "))
# print("Country in the position:", num, "is", country[num])

# sport = ["fotball", "box"]
# fav_sport = input("Enter your favourite sport type: ")
# sport.append(fav_sport)
# sport.sort()
# print(sport)

# subject = ["math", "geometry", "biology", "chemistry", "geology", "english"]
# dlike = input("Which of these subjects you don't like? ")
# subject.remove(dlike)
# print(subject)

# food = {}
# count = 0
# for i in range(0,4):
#     ffood = input("Enter your 4 favourite foods: ")
#     food[count] = ffood
#     count = count+1
# print(food)
# ranswer = int(input("Which from these you want to get rid: "))
# del food[ranswer]
# print(sorted(food.values()))

# color = ["black", "blue", "brown", "coral", "gold", "gray","green", "yellow", "blue", "red"]
# start = int(input("Enter starting number between 0 and 4: "))
# end = int(input("Enter starting number between 5 and 9: "))
# print(color[start:end+1])

# number_list = [111, 222, 333, 444]
# for i in number_list:
#     print(i)
# num = int(input("Enter 3 digit number: "))
# if num in number_list:
#     print(number_list.index(num))
# else:
#     print("That is not in the list!")

# people = []
# count = 3
# for i in range(0,3):
#     name = input("Enter names of 3 people that you want invite to the party: ")
#     people.append(name)
# answer = "False"
# while answer != True:
#     aname = input("Add more names?: ")
#     if aname.lower() == "yes":
#         name = input("Enter more: ")
#         people.append(name)
#         count = count + 1
#     elif aname.lower() == "no":
#         print(people)
#         print("You have invited: ", count, "people to the party")
#         break

# people = []
# count = 3
# for i in range(0,3):
#     name = input("Enter names of 3 people that you want invite to the party: ")
#     people.append(name)
# answer = "False"
# while answer != True:
#     aname = input("Add more names?: ")
#     if aname.lower() == "yes":
#         name = input("Enter more: ")
#         people.append(name)
#         count = count + 1
#     elif aname.lower() == "no":
#         print("Complete list of invited people:", people)
#         print("You have invited: ", count, "people to the party")
#         break
# index_people = input("Enter the name of person from the list: ")
# print("Positon of that person in the list: ", people.index(index_people))
# question = input("Do you still want that person to come to the party?: ")
# if question.lower() == "no":
#     people.remove(index_people)
#     print("New list is: ", people)


# tv_programms = ["58 Minutes", "The Chinaman", "Killed in Action ","Nothing Lasts Forever "]
# for i in tv_programms:
#     print(i)
# new_programm = input("Enter another TV show : ")
# position = int(input("and a position you want it inserted into the list: "))
# tv_programms.insert(position, new_programm)
# print("New list of TV shows: ")
# for i in tv_programms:
#     print(i)

# nums = []
# count = 0
# while count < 3:
#     num = int(input("Enter numbers: "))
#     nums.append(num)
#     print(nums)
#     count = count + 1
# last_number = input("If you still want the last number you entered to be saved?: ")
# if last_number == "no":
#     nums.remove(num)
# print(nums)
    
