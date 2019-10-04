# Import the os module to create file paths across operating systems
# Import the csv module for reading csv files 
import os
import csv

# Set path for file
csvpath = os.path.join("C:/Users/Jenni/UNCCDABC/Homeworks/python-challenge/PyPoll", "election_data.csv")

# Export print statements to a text file
#def log(message):
    #with open('C:/Users/Jenni/UNCCDABC/Homeworks/python-challenge/PyPoll/ElectionResults.txt', 'a+') as f:
        #f.write(message + "\n")
    #print(message)    

# Open the CSV, set variable that holds content and specify delimiter
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the headers first
    csv_reader = next(csvreader)

    # Initiate variable for elections results
    total_votes = 0
    # candidates_list = []
    poll = {}

    # Set for loop to get elections results
    for row in csvreader:

        total_votes +=1

        candidate_name = row[2]

        if candidate_name in poll.keys():
            poll[candidate_name] = poll[candidate_name] + 1
        else:
            poll[candidate_name] = 1
        #candidate_vote[candidate_name] = 0
        #candidate_vote[candidate_name] = candidate_vote[candidate_name] + 1

    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------")
    
    for candidate in poll:
         
        votes_per_candidate = poll.get(candidate)
        candidate_percentage = (votes_per_candidate / total_votes) * 100

        #if candidate_name not in candidates_list:
        #candidates_list.append(candidate_name)

        print(f"{candidate}: {candidate_percentage:.2f}%({votes_per_candidate})")
        #print(candidates_list)