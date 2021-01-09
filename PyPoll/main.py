import os
import csv

#Create a path to collect the data from the Resources folder
polls_csv = os.path.join("Resources","election_data.csv")

#Define our functions 
def print_electionresults(csvrow):

    voter_id = int(row[0])
    county = str(row[1])
    candidate = str(row[2])


#Read in the CSV file
with open(polls_csv, 'r') as csvfile

    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Loop through the data
    for row in csvreader: