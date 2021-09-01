# import csv file
import csv

# import to create paths with os = operating systems
# import pathlib
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

    # Variables Defined/empty lists (buckets)
    row_one = next(csvreader)
    total_months = 1
    net_total_profit = int(row_one[1])
    total_net_change = 0
    previous_value = int(row_one[1])
    max_increase = 0
    min_decrease = 0 
    max_increase_month = ''
    min_decrease_month = ''

    # Read each row of data after the header
    for row in csvreader:
        total_months += 1

        #summing the profit/losses for each month
        net_total_profit += int(row[1])
        
        #calcuate changes in profit/losses (current month - previous month)
        current_change = int(row[1]) - previous_value
        previous_value = int(row[1])

        #sum all variances (current changes)
        total_net_change += current_change

        #logic to find the max increase
        if current_change > max_increase:
            max_increase = current_change
            max_increase_month = row[0]
        
        #logic to find the min decrease
        if current_change < min_decrease:
            min_decrease = current_change
            min_decrease_month = row[0]
    
    # Total number of months included in the dataset
    print(total_months)

    # The net total amount of "Profit/Losses" over the entire period
    print(net_total_profit)
    
    # The average of the changes in "Profit/Losses" over the entire period
    avg_change = total_net_change/(total_months - 1)
    print(avg_change)
        
    # The greatest increase in profits (date and amount) over the entire period
    print(max_increase)
    print(max_increase_month)
        
    # The greatest decrease in losses (date and amount) over the entire period
    print(min_decrease)
    print(min_decrease_month)



    results = f'''
    Financial Analysis\n
    ----------------------------\n
    Total Months: {total_months}\n
    Total: ${net_total_profit:.2f}\n
    Average Change: ${avg_change:.2f}\n
    Greatest Increase in Profits: {max_increase_month} (${max_increase})\n
    Greatest Decrease in Profits: {min_decrease_month} (${min_decrease})\n
    '''


    # Export the results to text file
    with open("results.txt", "w") as file:
        file.write(results)