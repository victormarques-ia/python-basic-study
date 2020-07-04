

# Variables

"""
In other programming languages like C, C++, and Java, you will need to declare the type of variables but in Python you don’t need to do that. Just type in the variable and when values will be given to it, then it will automatically know whether the value given would be an int, float, or char or even a String. """

print("======== Variables ========")
myNumber = 3
print(myNumber)

myNumber2 = 4.5
print(myNumber2)

myNumber = "Hello World"
print(myNumber)

# Data Structures
"""
Python have 4 types of built in Data Structures namely List, Dictionary, Tuple and Set. 

List is the most basic Data Structure in python. List is a mutable data structure i.e items can be added to list later after the list creation. It’s like you are going to shop at the local market and made a list of some items and later on you can add more and more items to the list.
append() function is used to add data to the list.
"""

print("======== List Data Structure ========")
# creates a empty list
nums = []

#appending data in list
nums.append(21)
nums.append(40.5)
nums.append("String")

print(nums)