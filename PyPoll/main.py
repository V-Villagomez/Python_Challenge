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


    # Create dictionary to append candidate names and number of votes each candidate received 
    votes_dict = {}

    # Read through each row of data after the header
    for row in csvreader:
        
        # The total number of votes cast
        total_votes += 1
        
        # Create poll dictionary
        # Get complete list of candidates who received votes
        if row[2] in votes_dict.keys():
            votes_dict[row[2]] += 1
        else: 
            votes_dict[row[2]] = 1

    print(total_votes)
    #print(votes_dict)

    # Create additional variables 
    winner_votes = 0   #variable to help find winner, starts w/ 0, as look at candidate votes, update this variable, as loop find highest number votes
    winner_name = ""

    # Get the vote count and percentage
    for k, v in votes_dict.items():
        print(f'{k}: {round(v/total_votes * 100, 3)}% ({v})')
    
    # Find the winner
        if v > winner_votes:
            winner_votes = v
            winner_name = k

    print(f'The Winner is: {winner_name} with {winner_votes} votes')



#Analysis below:

# Export the results to text file


    results = f'''
    Election Results

    ----------------------------
    
    Total Votes: {total_votes}
    
    ----------------------------\n'''
    
    votes_text = ""
    for k, v in votes_dict.items():
        votes_text += f'    {k}: {round(v/total_votes * 100, 3)}% ({v})\n'

    results += votes_text
    results += f'''
    ----------------------------

    The Winner is {winner_name} with {winner_votes} votes

    ----------------------------
    '''

   
    with open("results.txt", "w") as file:
        file.write(results)