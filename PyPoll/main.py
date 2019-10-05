# Import the os module to create file paths across operating systems
# Import the csv module for reading csv files 
import os
import csv

# Set path for file
csvpath = os.path.join("C:/Users/Jenni/UNCCDABC/Homeworks/python-challenge/PyPoll", "election_data.csv")

# Export print statements to a text file
def log(message):
    with open('C:/Users/Jenni/UNCCDABC/Homeworks/python-challenge/PyPoll/ElectionResults.txt', 'a+') as f:
        f.write(message + "\n")
    print(message)    

# Open the CSV, set variable that holds content and specify delimiter
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the headers first
    csv_reader = next(csvreader)

    # Initiate variable for elections results
    total_votes = 0
    poll = {}
    winner_votes = 0
    winner = ""

    # Set for loop to get total votes and votes per candidate
    for row in csvreader:

        total_votes +=1

        candidate_name = row[2]

        if candidate_name in poll.keys():
            poll[candidate_name] = poll[candidate_name] + 1
        else:
            poll[candidate_name] = 1

    # Print total votes in the election
    log("Election Results")
    log("---------------------------")
    log(f"Total Votes: {total_votes}")
    log("---------------------------")
    
    # Set for loop to get votes and percentage for each candidate.
    # Also, get the winner of the election.
    for candidate in poll:

        votes_per_candidate = poll.get(candidate)
        candidate_percentage = (votes_per_candidate / total_votes) * 100

        log(f"{candidate}: {candidate_percentage:.3f}% ({votes_per_candidate})")
        #print(candidates_list)

        if votes_per_candidate > winner_votes:
            winner_votes = votes_per_candidate
            winner = candidate

    log("---------------------------")
    log(f"Winner: {winner}")
    log("---------------------------")