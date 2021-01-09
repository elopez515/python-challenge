import os
import csv
#Path to collecet data form our Resources folder
budgets_csv = os.path.join("Resources", "budget_data.csv")

#Define the functions and accept 'budget_data' as the sole parameter
def print_budgets(csvrow):

    dates = str(row[0])
    profit_losses = int(row[1])

   #define the start date of our data set 
    import datetime
    start_date = datetime.datetime(2010,1,1)

   #define the end date of our data set 
    end_date = datetime.datetime(2017,2,1)
   
   #clculate the total number of months in our data set
    total_months = (end_date.year - start_date.year)*12 + (end_date.month - start_date.month)

    print(total_months)


#read in the csv file
with open(budgets_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')