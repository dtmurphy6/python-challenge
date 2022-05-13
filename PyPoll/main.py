#import modules
import os
import csv

#variables
votes = []
total_votes = 0
candidate = ""
unique_candidates = []
candidate_votes = {}
counties = []
county_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#set CSV file path
csvpath = os.path.join('Resources', 'election_data.csv')

#read through CSV to pull data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header row
    csv_header = next(csvfile)

    #add votes to votes list, track unique candidates
    for row in csvreader:
        votes.append(row[0])
        candidate = row[2]
        counties.append(row[1])

        #determine if candidate is unique and create a votes dictionary entry for that candidate
        if candidate not in unique_candidates:
            unique_candidates.append(candidate)
            candidate_votes[candidate] = 0

        candidate_votes[candidate] += 1

    #determine total votes
    total_votes = len(votes)