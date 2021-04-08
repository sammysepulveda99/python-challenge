#Import the os module to create file paths across operating systems
import os
#Module for reading CSV
import csv
csvpath = os.path.join('PyPoll','Resources',"election_data.csv")

#Counter for votes
total_votes = 0

#Number of candidates
total_candidates = 0

#List of number of votes
number_votes = {}
# List of percentage of votes
percentage_votes=[]
#List of candidates
candidate_list = []
#Counter for winner vote
winner_votes= 0

#Winner
winner=""



#Improved reading with CSV module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

#Add a vote for a candidate if they are on on the list, if they are not on the list, add his name
#and a vote along with it to the list

    for row in csvreader:
        total_votes += 1   
        total_candidates = row[2]

        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            index= candidate_list.index(row[2])
            number_votes[row[2]] = 1
            
        else:
            number_votes[row[2]] = number_votes[row[2]] + 1
    
# Results
    print("Election Results")
    output.write("Election Results")
    print("--------------------------")
    output.write("--------------------------")
    print(f"Total Votes: {str(total_votes)}")
    print("--------------------------")
    print("--------------------------")

    
    
    #Calculating percentage of votes

    for candidates in number_votes:
        percentage = (number_votes.get(candidates)/total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percentage_votes.append(percentage)
        votes= number_votes.get(candidates)
       
       #Finding the maximum winner
        if votes  > winner_votes:
            winner_votes=votes
            winner=candidates   
        print(f"{candidates}: {str(percentage)} ({str(votes)})")
        print("--------------------------")
    print(f"Winner: {winner}")
    print("--------------------------")

# Exporting a .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
output.write()
for i in range(len(candidate_list)):
    line = str(f"{candidate_list[i]}: {str(percentage_votes[i])} ({str(number_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winner}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
