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
    net_change_profit_losses = 0
    previous_profit_losses = 0
    profit_losses_change = 0
    profit_losses_change_count = 0    

    #Loop through the data in our csvfile
    for row in csv_reader:

        #calculate for the net total of profit/losses
        current_profit_losses = int(row[1])
        net_total_profit_losses += current_profit_losses

       #Calculate the total amount of months
        total_months += 1


        #Loop through the data to calculate for monthly change of profits/losses..
        #... and the total amount of monthly changes in profit_losses_change_count
        if previous_profit_losses != 0:
            profit_losses_change = current_profit_losses - previous_profit_losses
            net_change_profit_losses += profit_losses_change
            profit_losses_change_count += 1

        #Reset the variable so that the next month is subtracted by its preceding month
        previous_profit_losses = current_profit_losses 

    #calculate the average change using values found in the for previous loop
    average_change = net_change_profit_losses/profit_losses_change_count

    print(average_change)
    print(net_total_profit_losses)
    print(total_months)