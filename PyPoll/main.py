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
    #print(f"Header: {csv_header}")

    #Define our varirables 
    total_votes = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    O_Tooley_votes = 0
    max_votes = 0
    winner = 0 

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

    #Create a dictionary holding each candidate respective total votes
    dict_candidate_and_votes = {
        "Khan": Khan_votes ,
        "Correy": Correy_votes ,
        "Li": Li_votes ,
        "O'Tooley": O_Tooley_votes
    }
    #print(candidate_and_votes_dict)
    
    #Determine who won the election
    for candidate, votes in dict_candidate_and_votes.items():
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    # print(winner)
    # print(total_votes)
    # print(Khan_votes)
    # print(Correy_votes)
    # print(Li_votes)
    # print(O_Tooley_votes)
    # print(Khan_votes_pct)
    # print(Correy_votes_pct)
    # print(Li_votes_pct)
    # print(O_Tooley_votes_pct)


# print(f'Election Results')
# print(f'------------------------')
# print(f'Total Votes: {total_votes}')
# print(f'------------------------')
# print(f'Khan: {Khan_votes_pct}% ({Khan_votes})')
# print(f'Correy: {Correy_votes_pct}% ({Correy_votes})')
# print(f'Li: {Li_votes_pct}% ({Li_votes})')
# print(f'"O'"'"f'Tooley: {O_Tooley_votes_pct}% ({O_Tooley_votes})')
# print(f'------------------------')
# print(f'Winner: {winner}')
# print(f'------------------------')

Election_Results = f"""
Election Results
------------------------
Total Votes: {total_votes}
------------------------
Khan: {Khan_votes_pct}% ({Khan_votes})
Correy: {Correy_votes_pct}% ({Correy_votes})
Li: {Li_votes_pct}% ({Li_votes})
O'Tooley: {O_Tooley_votes_pct}% ({O_Tooley_votes})
------------------------
Winner: {winner}
------------------------
"""
print(Election_Results)

#Specifying  the file to write to
output_path = os.path.join("Analysis", "Election_Results.txt")

#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as txtfile:

    writer = txtfile.write(Election_Results)
