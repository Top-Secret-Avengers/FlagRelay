# read the csv and create a list with all answers and hints
import csv

# file = open("demo.csv","r")

with open('demo.csv') as file:
    test = csv.reader(file)

for row in test:
    print(row)


# initialize dictionary for leaderboard