# Import the os module to create file paths across operating systems
# Import the csv module for reading csv files 
import os
import csv

# Set path for file
csvpath = os.path.join("C:/Users/Jenni/UNCCDABC/Homeworks/python-challenge/PyBank", "budget_data.csv")

# Export print statements to a text file
def log(message):
    with open('C:/Users/Jenni/UNCCDABC/Homeworks/python-challenge/PyBank/FinancialAnalysis.txt', 'a+') as f:
        f.write(message + "\n")
    print(message)    

# Open the CSV, set variable that holds content and specify delimiter
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the headers first
    csv_reader = next(csvreader)

    # Initiate variables for financial analysis
    dates = []
    profit_loss = []
    change_profit_loss = []

    # Set for loop for total amount of months and net total amount of "Profits/Losses".
    for row in csvreader:
        dates.append(row[0])
        profit_loss.append(float(row[1]))

    # Print statements
    log("Financial Analysis")
    log("---------------------------")
    log("Total Months: " + str(len(dates)))
    log("Total: $" + str(sum(profit_loss)))

    # Set for loop to get toal change in "ProfitsLosses", maximum increase in profits and
    # maximum decrease in profits.
    for i in range(1, len(profit_loss)):
        change_profit_loss.append(profit_loss[i] - profit_loss[i - 1])
        average_change_profit_loss = round((sum(change_profit_loss) / len(change_profit_loss)), 2)

        max_increase = max(change_profit_loss)
        max_decrease = min(change_profit_loss)

        max_increase_date =  dates[change_profit_loss.index(max(change_profit_loss))]
        max_decrease_date = dates[change_profit_loss.index(min(change_profit_loss))]

    # Print statements for average change, greatest increase and greatest decrease in "Profits/Losses".
    log("Average Change: $" + str(average_change_profit_loss))
    log("Greatest Increase in Profits: " + max_increase_date + " ($" + str(max_increase) + ")")
    log("Greatest Decrease in Profits: " + max_decrease_date + " ($" + str(max_decrease) + ")")