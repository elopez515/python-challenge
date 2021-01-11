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
    #print(f"Header: {csv_header}")

    #Define our variables
    total_months = 0
    net_total_profit_losses = 0
    net_change_profit_losses = 0
    previous_profit_losses = 0
    profit_losses_change = 0
    profit_losses_change_count = 0    
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_date = ""
    greatest_decrease_date = ""

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

        #Loop through the data to find greatest increase/decrease in profit/losses...
        #... along with their respective dates
        if profit_losses_change > greatest_increase:
            greatest_increase = profit_losses_change
            greatest_increase_date = row[0]
        if profit_losses_change < greatest_decrease:
            greatest_decrease = profit_losses_change
            greatest_decrease_date = row[0]

    #calculate the average change using values found in the for previous loop
    average_change = round((net_change_profit_losses/profit_losses_change_count),2)

    # print(greatest_decrease)
    # print(greatest_decrease_date)
    # print(greatest_increase_date)
    # print(greatest_increase)
    # print(average_change)
    # print(net_total_profit_losses)
    # print(total_months)

financial_analysis = f"""
Financial Analysis
-----------------------
Total Months: {total_months}
Total: ${net_total_profit_losses}
Average  Change: ${average_change}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})
"""
print(financial_analysis)