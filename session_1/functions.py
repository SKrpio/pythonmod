# Local and Global variables 

# Functions we've already seen - input(), len(), print(), int ()

# name = input("What is your name?")
# age = input("How old are you?")
# if age >= 18:
#     print("Welcome")
# else: ("You can not enter")

# Task Seperation

# def ask_user_name():
#     name = input("What is your name?")
#     return name  #return will end function - cant put anything after

# answer = ask_user_name("What is your name?")

# def ask_user_age():
#     age = input("How old are you?")
#     if age >= 18:
#         print("Welcome")    
#     else: ("You can not enter")

# Parameters
# def add(number1, number2): #number1 = 2 number2 = 3 
#     result = number1 + number2
#     return result
# answer = add(2,3) 
# print(answer)

#Variable inside a function is LOCAL - it does not exist outside the function

#Q1

# prompt = input("Could I have an integer?")
# input = prompt
# print(f"So your integer is {input}? Thanks")

#Q2 THIS IS CORRECT AND DOES USE A FUNCTION

# temperature = int(input("What is the temperature (Fahrenheit)? : "))
# print(f"Okay, so the temp in Fahrenheit is {temperature}...")
# def convert():
#     answer = float((temperature-32)*5/9)
#     print(f"Which means the temp in Celcius is {answer}")
# convert()

# THIS IS CORRECT BUT DOES NOT USE A FUNCTION ... 
# temperature = int(input("What is the temperature (Fahrenheit)? : "))
# print(f"Okay, so the temp in Fahrenheit is {temperature}...")
# answer = float((temperature-32)*5/9)
# print(f"Which means the temp in Celcius is {answer}")


# Q3 

