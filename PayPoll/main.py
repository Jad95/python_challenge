import csv

# path to the csv file
file_path = "D:/Data analytics bootcamp/week3/module_3_challenge/python_challenge/PayPoll/resources/election_data.csv"

# initialize variables
count_votes = 0
vote_counts = {}
candidates = []

# read the csv file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) # skip header row
    
    # loop through rows
    for row in csvreader:
        # vote count
        count_votes += 1
        
        # candidate vote count
        if row[2] in vote_counts:
            vote_counts[row[2]] += 1
        else:
            vote_counts[row[2]] = 1
            
        # list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            
# calculate percentage of votes and total votes per candidate
percentage_votes = {}
total_votes = 0
for candidate, votes in vote_counts.items():
    percentage_votes[candidate] = '{0:.2f}%'.format((votes/count_votes)*100)
    total_votes += votes

# determine winner based on popular vote
winner = max(vote_counts, key=vote_counts.get)


# print results
output = "Election Results\n"
output += "-------------------------\n"
output += "Total Votes: " + str(count_votes) + "\n"
output += "-------------------------\n"
for candidate in candidates:
    output += candidate + ": " + str(percentage_votes[candidate]) + " (" + str(vote_counts[candidate]) + ")\n"
output += "-------------------------\n"
output += "Winner: " + winner + "\n"
output += "-------------------------\n"

# print results to terminal
print(output)

# write results to txt file
with open("D:/Data analytics bootcamp/week3/module_3_challenge/python_challenge/PayPoll/analysis/election_results.txt", "w") as txt_file:
    txt_file.write(output)