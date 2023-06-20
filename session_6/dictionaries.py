#Lists 
# numbers = [1,2,3]
# numbers [0]
# Dictionary 
# Stores key and value PAIRS "cindy" is key "111" is value
# Keys are unique!
# Values can be any datat type
# Keys can only be immutable data types
# Immutable = strings, integers, floats, booleans
# student_phonebook = {
#     "Cindy":111,
#     "Tracey":123,
#     "Sarah":444,
#     }
# print(student_phonebook)
# student_phonebook["Yara"] = 555 #adds extra to list
# print(type(student_phonebook))

# print(student_phonebook)
# student_phonebook["Cindy"]=555 #Overwrite value given
# print(student_phonebook)

# del student_phonebook["Tracey"] #Delete from list

# student_phonebook = {
#     "Cindy":111,
#     "Tracey":123,
#     "Sarah":444,
#     }

# for element in student_phonebook:
#     print(element)
#above prints just keys

# for key in student_phonebook:
#     print(key, student_phonebook [key])
#prints key and values

# for value in student_phonebook.values():
#     print(value)
#prints just values



# a, b = [1,2]
# print(a)
# print(b)
# for key,value in student_phonebook.items():

#     print(key,value)

#Tuple can hold multiple values separated by comma
# 1st item in tuple always key, 2nd always value


# Q1    # This works - but is there a shorter way?

# groceries = {
#     "Baby Spinach": 2.78,
#     "Hot Chocolate": 3.70,
#     "Crackers": 2.10,
#     "Coffee": 9.00,
#     "Carrots": 0.56,
#     "Oranges": 3.08
# } 
# spinach = groceries ["Baby Spinach"]
# spinach_amount = int(input("How much Baby Spinach did I buy? : "))
# spinach_total = spinach * spinach_amount

# chocolate = groceries ["Hot Chocolate"]
# chocolate_amount = int(input("How much Hot Chocolate did I buy? : "))
# chocolate_total = chocolate * chocolate_amount

# crackers = groceries ["Crackers"]
# crackers_amount = int(input("How many Crackers did I buy? : "))
# crackers_total = crackers * crackers_amount

# coffee = groceries ["Coffee"]
# coffee_amount = int(input("How much Coffee did I buy? : "))
# coffee_total = coffee * coffee_amount

# answer = float(spinach_total + chocolate_total + crackers_total + coffee_total)
# print(f"My groceries cost me {answer} ")

# Q2  - failed attempt

# colour_counts = {
#     "blue": 0,
#     "green": 0,
#     "yellow": 0,
#     "red": 0,
#     "purple": 0,
#     "orange": 0,
#     }

# import csv
# with open('colours_865.csv', newline='') as csvfile:
#     data = csv.DictReader(csvfile)
#     for colour_counts in data:
#         print(f"Appeared {colour_counts} times")

# Q2 not using dictionary
# yellow = "Yellow"
# green = "Green"
# blue = "Blue"
# red = "red"
# purple = "purple"
# orange = "orange"

# file = open("colours_865.csv", mode ="r")
# read_data = file.read()
# yellow_count = read_data.count(yellow)
# green_count = read_data.count(green)
# blue_count = read_data.count(blue)

# total = yellow_count + green_count + blue_count
# print(f"Yellow, Green & Blue appeared {total} times")

# Q3 
# file = open("colours_20_simple.csv", mode = "r")
# read_data = file.read()

