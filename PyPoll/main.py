#import modules
from inspect import BoundArguments
import os
import csv

#variables
total_votes = 0
candidate = []
candidate_votes = {}
votes = ""
percentage = 0
most_votes = 0
winner = ""

#set CSV file path
csvpath = os.path.join('Resources', 'election_data.csv')

#read through CSV to pull data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header row
    csv_header = next(csvfile)

    #add votes to votes list, track unique candidates
    for row in csvreader:
        total_votes += 1

        #determine if candidate is unique and create a candidate votes dictionary entry for that candidate
        if row[2] not in candidate:
            candidate.append(row[2])
            candidate_votes[row[2]] = 0
        
        #add a vote to current candidate's count
        candidate_votes[row[2]] += 1

#print output            
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
#determine vote percentage, print it, and determine winning candidate
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = int(votes) / total_votes * 100
    print(str(candidate) + ": " + str(round(vote_percentage, 3)) + "% (" + str(votes) + ")")
    if votes > most_votes:
        most_votes = votes
        winner = candidate
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

#output to a text file
file = open("Analysis/output.txt", "w")
file.write("Election Results" + "\n")
file.write("-------------------------" + "\n")
file.write("Total Votes: " + str(total_votes) + "\n")
file.write("-------------------------" + "\n")
#determine vote percentage, output it, and determine winning candidate
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = int(votes) / total_votes * 100
    file.write(str(candidate) + ": " + str(round(vote_percentage, 3)) + "% (" + str(votes) + ")" + "\n")
    if votes > most_votes:
        most_votes = votes
        winner = candidate
file.write("-------------------------" + "\n")
file.write("Winner: " + winner + "\n")
file.write("-------------------------")

