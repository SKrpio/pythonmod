# letters = ['a','b','c']

# Loops help us to perform a task multiple times
# There are two types of loops

#Number 1 - While Loops
#as long as this condition is true, then "Hello"

# count = 1
# while count != 4: 
#     print("Hello")
#     count = count + 1 

# count = 0
# while count <= 6: 
#     print("Hello")
#     count = count + 1 



# count + 1 adds one every loop until while statement no longer true - ends loops

#Q1
# number = input("Gimme a number")
# sum = 0 
# while number:
#     sum = sum + int(number)
#     number = input("gimme another number")
# print(sum)


# Q2 

# number = input("Enter number")
# list_of_numbers = range(int(number)+1)
# odd_numbers_list = []
# for number in list_of_numbers:
#     if number % 2 == 0:
#         pass
#     else:
#         odd_numbers_list.append(number)
# print(odd_numbers_list)

# answer = 22
# guess = input("Guess a number")
# if guess != answer:
#     guess = input ("Wrong, guess again")
# else:
#      guess == answer:            # what is wrong here??
# print("That is correct!")



# i = 1
# while i < 5:
#  print(i)
#  i += 1

# THIS IS RIGHT BUT NOT FINISHED
# answer = ''
# while answer != '22':
#     print('Guess my number?')
#     answer = input()
# print('Yes, the answer is ' + answer + '. You may enter.')


## YOUTUBE TUTORIAL THAT STILL FAILED
# answer = 22
# guess_count = 100
# limit = 100000000
# while guess_count < limit:
#     guess = (input('Guess my number'))
#     guess += 1
#     if guess == answer:
#         print('You win!')
#         break
# else:
#     print('Holy fk u failed')

# ATTEMPT NUMBER 452 - NOT WORKING
# answer = 22
# int(input("Guess my number?"))
# while int < answer:
#     int(input('Too low, guess again?'))
#     if int > answer:
#         int(input("Too high, guess again?"))
#         break

# answer = 22
# guess = int(input("Guess my number: "))
# while answer != guess:
#     if guess < answer:
#         print("Too low")
#         guess = int(input("Guess again?"))
#     elif guess > answer:
#         print("too high")
#         guess = int(input('Guess again?'))
#     else:
#         break
# print("You guessed it!")

# Q2 ORIYAN'S C0DE
# print("The first number is 0")
# large_number = int(input("Enter a number: "))
# while large_number > 0:
#     if(large_number % 2 != 0):
#         print(large_number)
#     large_number = large_number - 1

# MY BOYFRIEND'S HELPING ME NOW - STILL NOT FINISHED THO
# answer = ''
# guess = input("Guess my number")
# while guess != '22':
#     guess = input ('Guess again?')
#     input == guess
# print('Yes, the answer is ' + answer + '. You may enter.')

# count = 0
# while count <= 6: 
#     print("Hello")
#     count = count + 1


# count = int(input("Enter a number"))
# twocount = int(input("Enter a number"))
# count = count + twocount
# print(f"Your numbers equal {count}")

# name = input("What is your name?")
# while name !="Bear":
#     print("I dont know you")
#     name = input("What is the new name?") 

#Number 2 - For Loops

# for letter in letters:
#     print(letters) 

# range (0,10) will run through all numbers
# range function similar to slicing

# students = [
#     ["bob", "jim", "todd"]
# ]
# for student in students:
#     print(student)
#     for name in student:
#         print(name)

# num = input ("Enter a number")
# secondnum = input ("Enter a number")
# print(f"Your numbers sum to{num + secondnum}")


# For Loops - Q1 - Cinzia's Code 

# to_multiply = int(input("Give me a number: "))
# for number in range(1,11):
#     print(f"{to_multiply} x {number} = {to_multiply*number}")

# For Loops - Q2 - Maya 

# max_number = int(input("Enter number and ill add up everything before it"))
# total = 0 
# for number in range(0, max_number+1):
#     total += number
# print (total)

# For Loops Q3  - I did it!
# digits = (1, 2, 3, 4)
# for number in digits:
#     print(sum(digits))
#     break


# def add(number1, number2): #number1 = 2 number2 = 3 
#     result = number1 + number2
#     return result
# answer = add(2,3) 
# print(answer)

# For Loops Q4 - I DID IT
# start = ("A little bit of")
# mambo = ["Monica in my life", "Erica by my side","Rita's all I need", "Tina's what I see", "Sandra in the sun",    
# "Mary having fun", "Jessica here I am"]
# for mambo in mambo:
#  print(start, mambo)
# print("a little bit of you makes me your man (ah!)")
# print("*trumpet solo")


# alphabet = ['a' ,'b', 'c']
# for letter in alphabet:
#     print(letter)


# for i in range(1, 5):
#  print(i)

#Nested Loops Q1

groceries = [   
     ["Baby Spinach", 2.78],   
     ["Hot Chocolate", 3.70],    
     ["BBQ Shapes", 9.00],   
     ["Bread", 2.10],    
     ["Carrots", 0.56],    
     ["Oranges", 3.08]
     ]

# total_price = 0

# # loop first time
# Spinach = input("How many Baby Spinach? : ")
# total_price = total_price + (int(Spinach) *2.78  )

# # loop second time
# Chocolate = input("How many Chocolate? : ")
# total_price = total_price + (int(Chocolate) * 3.70)

# # loop third time
# Bread = input("How many Bread? : ")
# total_price = total_price + (int(Bread) * 2.10)


total_price = 0
for ingredient_and_price_list in groceries:
    # ingredient_and_price_list = ['Baby Spinach', 2.78]
    # ingredient_and_price_list = ['Hot Chocolate', 3.7]
    # input line
    ingredient = input(f'How many {ingredient_and_price_list[0]}:')
    # totaly price math
    total_price = total_price + (int(ingredient) * ingredient_and_price_list[1])

# for grocery in groceries:
#     print('loop start')
#     print(grocery)
#     print('loop end')