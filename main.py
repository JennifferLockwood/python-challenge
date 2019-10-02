# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

# Prompt user for video lookup
# video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("C:/Users/Jenni/UNCCDABC/Homeworks/python-challenge", "budget_data.csv")

# Open the CSV, set variable that holds content and specify delimiter
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the headers first
    csv_reader = next(csvreader)

    #Set total amount of months, total of "Profit/Losses"
    totalMonths = 0
    totalProfitLosses = 0

    for row in csvreader:
        # month = (row[0].split("-"))
        totalMonths += 1
        profitLosses = int(row[1])
        totalProfitLosses += profitLosses
        # print(month[0])
        # print(row[0].split("-"))

    # Print final statements
    print("Financial Analysis")
    print("---------------------------")
    print("Total Months: " + str(totalMonths))
    print("Total: $" + str(totalProfitLosses))

    # print(csvreader)