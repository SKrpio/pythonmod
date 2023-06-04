#Boolean
# name = "Sarah"
# age = 25
# heihgt = 1.85
# is_raining = True
# my_variable2 = False

#Boolean expression - expression that produce a boolean value
# Comparison operators
# == is equal
# != is not equal to
# > greater than
# < less than 
# >= greater or equal to 
# <= less than or equal to
# print(5>3) 
# print(3.5 > 6.3)
# print("Asli" == "asli")

#Mathematical operators - Addition, Division, Subtraction and Multiplication
# Boolean operators - not, and, or
# is_sunny = True
# print(not is_sunny)
# is_warm = True
# print(is_sunny and is_warm)
# print(is_sunny or is_warm)

# temperature = 19
# #syntax and semantics
# if temperature > 18:
#     print("Weather is nice!")
# elif temperature >28: #if statement false, it will check elif
#     print("Weather is too hot")
# else:
#     print("Weather is bad")

#multiple if statements, will check all statements

# sara_has_helmet = True
# rei_rope = False
# if sara_has_helmet and rei_rope == True:
#     print("Let's send it")
# if sara_has_helmet == False and rei_rope == True:
#     print("No way, my brain is my moneymaker")
# if sara_has_helmet == True and rei_rope == False:
#     print("Who's unprepared now?")
# else: 
#     print("Let's go hiking")

# light_color = "amber"
# car_detected = False
# if car_detected == False and car_detected == "red":
#     print("Do nothing")
# if car_detected == True and light_color == "red":
#     print ("Flash!")
# if light_color == "amber" and car_detected == False:
#     print("Do nothing")

# store multiple data points, can take different data types
digits = [1,2,3,4,5] #str, int, float, list
# print(list_name)
# print (type(list_name))

#lists are index based which start from 0 i.e 0 = 1

# print(digits[4])
# print(digits[-1]) #will return last element

#Slicing a list - for multiple elements
# print(digits[0:4]) #start is always inclusive and end is always exclusive
# print(digits[3:])
# print(digits[0:5:2])

# print(len(digits))
# print(digits)
# digits.append(6)
# print(digits)
# popped_element = digits.pop(0)
# digits[1] = 90
# print(digits)

# letters = ['a','b','c','d',['Emily','Julie']]
# print(letters[4][0]) #Get the first in the list, then get the first element from another list

# if 'a' in letters:
#     print("It is in the list")

# foods = ["orange","apple","banana","strawberry",
#          "grape","blueberry",    
#          ["carrot", "cauliflower", "pumpkin"],
#          "passionfruit","mango","kiwifruit"]
# print(foods[0:3]) #first three in list
# print(foods[7:12]) last three in list 
# print(foods[6][2]) #print last item in sublist

# start = "A little bit of"
# mambo = [    
#         ["Monica", "in my life"],    
#         ["Erica", "by my side"],    
#         ["Rita's", "all I need"],    
#         ["Tina's", "what I see"],    
#         ["Sandra", "in the sun"],    
#         ["Mary", "having fun"],    
#         ["Jessica", "here I am"]
# ]
# print(start, mambo[0][0],mambo[0][1])
# print(start, mambo[1][0],mambo[1][1])
# print(start, mambo[2][0],mambo[2][1])
# print(start, mambo[3][0],mambo[3][1])
# print(start, mambo[4][0],mambo[4][1])
# print(start, mambo[5][0],mambo[5][1])
# print(start, mambo[6][0],mambo[6][1])
# print(start, "you makes me your man (ah!)")
# print("*trumpet solo*")

# name = input("Write three names")
# input(name)

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = []
e = []

print(a,b,c)
print(a[0:],b[0:],c[0:])




