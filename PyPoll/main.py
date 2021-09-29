# Create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote 

# dependencies
# import csv file
import csv

# import to create paths with os = operating systems
# import pathlib
import os
import pathlib

csvpath = pathlib.Path('Resources/election_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f'Header: {csv_header}')

    # Variables Defined/empty lists (buckets)
    total_votes = 0        #number of votes
    candidate_list = []    #list of all candidates
    candidate = []
    vote_percentage = []
    vote_count = []
    winning_votes = 0      #correspond to number of votes
    winner = ""            #empty string to be changed to name of winner

    # Create dictionary to append candidate names and number of votes each candidate received 
    votes_dict = {}

    # Read through each row of data after the header
    for row in csvreader:
        
        # Total vote count
        total_votes += 1
        
        # Create poll dictionary
        # Get complete list of candidates who received votes
        if row[2] in votes_dict.keys():
            votes_dict[row[2]] += 1
        else: 
            votes_dict[row[2]] = 1
        #print(votes_dict) 
        
        # Get the candidate name from each row
        #candidate_name = row[2]

        # If candidate is not in dictionary, add candidate to list and track that candidate's vote count 
        #if candidate_name not in candidate_list:
            #candidate_list.append(candidate_name)
            #votes_dict[candidate_name] = 0
            #print(candidate_list)

        # Add a vote to the candidate's count
        #votes_dict[candidate_name] = votes_dict[candidate_name] + 1

    print(total_votes)
    #print(votes_dict)

    winner_votes = 0

    # Get the vote count and percentage
    for k, v in votes_dict.items():
        print(f'{k}: {round(v/total_votes * 100, 3)}% ({v})')


    # Find the winner count and candidate

        
    #print each candidate voter results

    
    # The total number of votes cast
    


# Export the results to text file

#with open("results.txt", "w") as file:
    #file.write(results)

#Analysis should look similiar to the one below:
#```text
  #Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------
  #```

    #results = f'''
    #Election Results
    #----------------------------\n
    #"Total Votes: {total_votes}\n"
    #----------------------------\n

 
   

    

        
        




