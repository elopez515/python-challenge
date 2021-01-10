import os
import csv

#Create a path to collect the data from the Resources folder
polls_csv = os.path.join("Resources","election_data.csv")

#Read in the CSV file
with open(polls_csv, 'r') as csv_file:

    #Split the data on commas
    csv_reader = csv.reader(csv_file, delimiter=',')

    #Read the header row first
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    #Define our varirables 
    total_votes = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    O_Tooley_votes = 0

    #Loop through the data in our csvfile to find..
    #...total votes and candidate votes
    for row in csv_reader:

        #use if function to calculate each candidate's votes
        if "Khan" in row[2]:
            Khan_votes += 1
        elif "Correy" in row[2]:
            Correy_votes += 1
        elif "Li" in row[2]:
            Li_votes += 1
        elif "O'Tooley" in row[2]:
            O_Tooley_votes += 1
        
            
        #set variable for total_votes
        total_votes += 1
        
    #Calculate the percentage of votes each candidate received
    Khan_votes_pct = round((Khan_votes/total_votes)*100,2)
    Correy_votes_pct = round((Correy_votes/total_votes)*100,2)
    Li_votes_pct = round((Li_votes/total_votes)*100,2)
    O_Tooley_votes_pct = round((O_Tooley_votes/total_votes)*100,2)


    # print(total_votes)
    # print(Khan_votes)
    # print(Correy_votes)
    # print(Li_votes)
    # print(O_Tooley_votes)
    print(Khan_votes_pct)
    print(Correy_votes_pct)
    print(Li_votes_pct)
    print(O_Tooley_votes_pct)


# print(f'Election Results')
# print(f'------------------')
# print(f'Total Votes: {total_votes}')
# print(f'------------------')
# print(f'Khan: {Khan_votes}')
# print(f'Correy:')
# print(f'Li:')
# print(f'O'"Tooley:" ')
# print(f'------------------')
# print(f'Winner:')
# print(f'------------------')