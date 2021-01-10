import os
import csv

#Path to collecet data form our Resources folder
budgets_csv = os.path.join("Resources", "budget_data.csv")

#read in the csv file
with open(budgets_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    
    #Read the header row first
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    #Loop through the data in our csvfile
    for row in csvfile:

         print(row)
         exit()
        
        #set variable for total_votes
        #total_votes += 1

# #Define the functions and accept 'budget_data' as the sole parameter
# def budgets_data(row):
#     months = str(row[0])
#     profit_losses = int(row[1])
   
#    #calculate the total number of months in our data set
#      total_months = len(months)
#     print(total_months)
#     print(budgets_data)
# #Define the function to calculate average profit/loss
# def average(profit_losses): 
#     length = len(profit_losses)
#     total = 0.0
# for profit_loss in profit_losses:

# return total / length

#     #Calculate the average profit/loss
#     print(average(profit_losses))