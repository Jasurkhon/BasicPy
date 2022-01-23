# numeric array challenges

from array import *
from ast import Try
import random

# nums = array('i', [1,2,5,4,3])
# newValue = int(input("Enter new value: "))
# nums.append(newValue)
# print(nums)
# print(nums.reverse())
# nums = sorted(nums)
# print(nums)
# print(nums.pop(0))

# numbers = array('i', [])
# print("Enter a list of five integers: ")
# for i in range(5):
#     number = int(input("Enter integer: "))
#     numbers.append(number)
# numbers = sorted(numbers)
# numbers.reverse()
# print(numbers)

# numbers = array('i', [])
# for i in range(5):
#     number = random.randint(1,10)
#     numbers.append(number)
# for i in numbers:
#     print(i)

# numbers = array('i',[])
# count = 0
# while count != 5:
#     number = int(input("Enter number: "))
#     if (number > 10 and number < 20):
#         numbers.append(number)
#         count = count + 1
#     else:
#         print("Outside the range")
# print("Thank you")
# for i in numbers:
#     print(i)

# numbers = array('i', [1,2,3,3,4])
# print(numbers)
# number = int(input("Enter one number from the array: "))
# print(number, "appers in the array", numbers.count(number), "times")

# num1 = array('i', [])
# for i in range(3):
#     number = int(input("Enter number: "))
#     num1.append(number)
# print(num1)
# num2 = array('i', [])
# for i in range(5):
#     number = random.randint(1,10)
#     num2.append(number)
# print(num2)
# num1.extend(num2)
# num1 = sorted(num1)
# for i in num1:
#     print(i)

# numbers = array('i', [])
# newarray = array('i', [])
# for i in range(5):
#     number = int(input("Enter number: "))
#     numbers.append(number)
# numbers = sorted(numbers)
# print(numbers)
# unumber = int(input("Select number from the array: "))
# numbers.remove(unumber)
# newarray.append(unumber)
# print(numbers)
# print("new array: ", newarray)

# numbers = array('i', [1,2,3,4,5])
# print(numbers)
# unumber = int(input("Select number from the array: "))
# tryAgain = False
# while tryAgain == False:
#     if unumber in numbers:
#         print("Position of chosen item: ",numbers.index(unumber))
#         tryAgain = True
#     else:    
#         unumber = int(input("Try again: "))

# numbers = array('f', [10.11, 20.12, 30.13, 40.14, 60.15])
# number = int(input("Enter number between 2 and 5: "))
# tryAgain = False
# while tryAgain == False:
#     if number >2 and number < 5:
#         tryAgain = True
#     else:
#         number = int(input("Error, Try again: "))
# for i in numbers:
#     answer = i/number
#     print(i, "/", number, "=",round(answer,2))

