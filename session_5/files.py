# default is mode = r & encoding = utf-8 so not neccessary to specify unless weird system
import csv
with open(file="links.csv",mode="r", encoding="utf-8") as my_file:
    csv_reader= csv.reader(my_file)
    for row in csv_reader:
        print(row)
