# simple_array = [[1,2,3], [4,5,6], [7,8,9]]
# print(simple_array[0])
# print(simple_array[1])
# print(simple_array[2])
# print("Elemenet with indexes (1,1) = ",simple_array[1][1])
# simple_array[0].append(10)
# simple_array[1].append(11)
# simple_array[2].append(12)
# print(simple_array[0])
# print(simple_array[1])
# print(simple_array[2])

# data = {"Susan": {"Math":100, "English":94, "C++":90}, 
#         "Alex" : {"Math":95, "English":98, "C++":100}}
# print(data["Susan"])
# print(data["Alex"])
# print("Susan's Math score = ",data["Susan"]["Math"])
# for i in data:
#     print(data[i]["Math"])
# data["Susan"]["English"] = 100
# print(data["Susan"]["English"])

# grades[name] = {"Math":mscore, "English":escore}
# for name in grades:
#     print((name), grades[name]["English"])

# del list[getRid]

# simple_indexing = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
# print(simple_indexing)

# simple_indexing = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
# print(simple_indexing[0])
# print(simple_indexing[1])
# print(simple_indexing[2])
# print(simple_indexing[3])
# row_select = int(input("Enter row from table(note indexing starts from 0): "))
# column_select = int(input("Enter column from table(note indexing starts from 0): "))
# print(simple_indexing[row_select][column_select])

# simple_indexing = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
# row_display = int(input("Which row you want to be displayed: "))
# print(simple_indexing[row_display])
# new_item = int(input("Enter new value of item to be added in that row: "))
# simple_indexing[row_display].append(new_item)
# print(simple_indexing[row_display])

# simple_indexing = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
# row_display = int(input("Which row you want to be displayed: "))
# print(simple_indexing[row_display])
# column_display = int(input("Which column in that row you want to be displayed: "))
# print(simple_indexing[row_display][column_display])
# change_value = input("Do dou want to change the value? ")
# if change_value.lower() == "y":
#     column_display = int(input("Which column in that row you want to be changed and displayed: "))
#     print(simple_indexing[row_display][column_display])
# else:
#     print("Thank you")

# sales = {"John": {"N": 3065, "S": 8463, "E": 8441, "W": 2694},
#         "Tom": {"N": 2345, "S": 1234, "E": 3478, "W": 6754},
#         "Anne": {"N": 2353, "S": 5424, "E": 3456, "W": 2355},
#         "Fiona": {"N": 1245, "S": 9087, "E": 2456, "W": 2356},}
# print(sales["John"])
# print(sales["Tom"])
# print(sales["Anne"])
# print(sales["Fiona"])

# sales = {"John": {"N": 3065, "S": 8463, "E": 8441, "W": 2694},
#         "Tom": {"N": 2345, "S": 1234, "E": 3478, "W": 6754},
#         "Anne": {"N": 2353, "S": 5424, "E": 3456, "W": 2355},
#         "Fiona": {"N": 1245, "S": 9087, "E": 2456, "W": 2356},}
# name = input("Enter name: ")
# region = input("Enter region: ")
# print(sales[name][region])
# new_value = int(input("New value to be changed: "))
# sales[name][region] = new_value
# print("New data of the sales for all regions of the name you chosed",sales[name])

# person = {}
# for i in range(4):
#     name = input("Enter the name of person: ")
#     age = int(input("Enetr the age of the person: "))
#     shoe_size = int(input("Enter shoe size of the person: "))
#     person[name] = {"Age": age, "Shoe": shoe_size}

# ask_name = input("Enter the name: ")
# print(person[ask_name])

# person = {}
# for i in range(4):
#     name = input("Enter the name of person: ")
#     age = int(input("Enetr the age of the person: "))
#     shoe_size = int(input("Enter shoe size of the person: "))
#     person[name] = {"Age": age, "Shoe": shoe_size}

# for name in person:
#     print((name), person[name]["Age"])

# person = {}
# for i in range(4):
#     name = input("Enter the name of person: ")
#     age = int(input("Enter the age of the person: "))
#     shoe_size = int(input("Enter shoe size of the person: "))
#     person[name] = {"Age": age, "Shoe": shoe_size}
# name_remove = input("Enter the name to remove: ")
# del person[name_remove]
# for name in person:
#     print((name), person[name])
