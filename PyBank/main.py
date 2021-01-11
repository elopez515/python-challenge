import os
import csv

#Path to collecet data form our Resources folder
budgets_csv = os.path.join("Resources", "budget_data.csv")

#read in the csv file
with open(budgets_csv, 'r') as csv_file:

    # Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    
    #Read the header row first
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    #Define our variables
    total_months = 0
    net_total_profit_losses = 0

    #Loop through the data in our csvfile
    for row in csv_reader:

        #calculate for the net total of profit/losses
        current_profit_losses = int(row[1])
        net_total_profit_losses += current_profit_losses


       #Calculate the total amount of months
        total_months += 1

    print(net_total_profit_losses)
    #print(profit_losses_change)
    print(total_months)