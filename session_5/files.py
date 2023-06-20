# default is mode = r & encoding = utf-8 so not neccessary to specify unless weird system
# import csv
# with open(file="links.csv",mode="r", encoding="utf-8") as my_file:
#     csv_reader= csv.reader(my_file)
#     for row in csv_reader:
#         print(row)


# nested_list [['I', 'think', 'dogs', 'are,', 'awesome!']
# ['My,', "dog's", 'name', 'is,', 'Jett!']
# []
# ['I', 'love', 'him!']]
# with open(file="hello.csv", mode="w") as my_file:
#     csv_writer = csv.writer(my_file)
#     csv_writer.writerow(["Hello","Hi"])

# import csv

# with open(file="2016_pilbara.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         print(line)

# population = []

# with open(file="2016_pilbara.csv") as csv_file:
#     csv_reader = csv.reader(csv_file)
#     for line in csv_reader:
#         population.append(line)

# print(population)

# for age_group in population:
#     print(f"{age_group[0]} * {age_group[1]}")

# with open(file="population.csv", mode="w") as csv_file:
#     csv_writer = csv.writer(csv_file,delimiter="-")

#     for age_group in population:
#         age_group,frequency = age_group
#         print(age_group)
#         print(type(age_group))
#         print(frequency)
#         print(type(frequency))
#         csv_writer.writerow([age_group[0], age_group[1]])

# QUESTION 1 - RIGHT
# import csv
# with open(file="colours_20.csv", mode="r") as my_file:
#     csv_reader = csv.reader(my_file)
#     for row in csv_reader:
#         print(row)

# QUESTION 2 - order English, Hex then RGB -  DONE

# import csv
# with open(file="colours_20.csv", mode="r") as csv_file:
#     csv_reader = csv.reader(csv_file,delimiter=" ")
#     for line in csv_reader:
#         print(f"{' '.join(line[2:])} {(line[1])} {line[0]}")

 
 # QUESTION 3 - COMPLETE 

search_word_count = "yellow"
search_word = "Green"
last_word = 'beige'
file = open("colours_20.csv", mode ="r")

# reading data of the file
read_data = file.read()
word_count = read_data.count(search_word_count)
second_word_count = read_data.count(search_word)
last_word_count = read_data.count(last_word)
print(f"The word '{search_word_count}' appeared {word_count} times.")
print(f"The word '{search_word}' appeared {second_word_count} times.")
print(f"The word ' {last_word} appeared {last_word_count} times")



              