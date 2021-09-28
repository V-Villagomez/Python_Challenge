# Create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote 


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
    total_votes = 0
    candidates = []
    vote_percentage = []
    total_votes_won = []
    winner = []
    candidate_list = []

    # Create dictionary to append candidate names and vote count. 
    votes_dict = {}

    # Read through each row of data after the header
    for row in csvreader:
        
        # Total vote count
        total_votes += 1

        # Create poll dictionary
        # Get total vote count for each candidate
        if row[2] in votes_dict:
            votes_dict[row[2]] += 1
        else: 
            votes_dict[row[2]] = 1
        print(votes_dict)    
    
    
    
    # The total number of votes cast
    # print(total_votes)




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