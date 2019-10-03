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

    # Initiating variables for financial analysis
    dates = []
    profitLosses = []
    changeProfitLosses = []

    # Set for loop for total amount of months and net total amount of "Profits/Losses".
    for row in csvreader:
        # month = (row[0].split("-"))
        dates.append(row[0])
        profitLosses.append(float(row[1]))
        # print(month[0])
        # print(row[0].split("-"))

    # Print statements
    print("Financial Analysis")
    print("---------------------------")
    print("Total Months: " + str(len(dates)))
    print("Total: $" + str(sum(profitLosses)))

    