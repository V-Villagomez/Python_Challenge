# import csv file
import csv

# import to create paths with os = operating systems
import os

import pathlib

csvpath = pathlib.Path('Resources/budget_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')

    # Read each row of data after the header
    for row in csvreader:
        # print(f'CSV Header: {csv_header}')
        print(row[0])
