import os
import csv


files = os.listdir()

now = os.getcwd()

csvpath = os.path.join(now, '.vscode\python_financial_data-main\PyPoll\Resources', 'election_data.csv')
txtpath = os.path.join(now, '.vscode\python_financial_data-main\PyPoll\Analysis')

candidate_options = []
candidate_votes = {}
total_votes = 0
winning_vote_count = 0
winning_candidate = ""

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:

        #print(row)
        # Calculate the number of total votes overall
        total_votes =  total_votes + 1

        # List all the candidates in the election
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            
            candidate_options.append(candidate_name)
            
            #Record the vote count of each candidate
            candidate_votes[candidate_name] = 0

            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        else: 
            candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
greatest_vote = ["", 0]
record = []

print("Election Results")
record.append("Election Results")
print("-------------------------")
record.append("-------------------------")
print("Total Votes: " + str(total_votes))
record.append("Total Votes: " + str(total_votes))
print("-------------------------")
record.append("-------------------------")


for key, value in candidate_votes.items():
    if value > greatest_vote[1]:
        greatest_vote[0] = key
        greatest_vote[1] = value
    
    
    vote_pct = "{:.3%}".format(candidate_votes[key] / total_votes)
    print(f'{key}: {vote_pct} ({value})')
    record.append(str(key) + ":" + " " + str(vote_pct) + " " + "(" + str(value) + ")")

print("-------------------------")
record.append("-------------------------")
print(f'Winner: {greatest_vote[0]}')
record.append("Winner: " + str(greatest_vote[0]))
print("-------------------------")
record.append("-------------------------")

os.chdir(txtpath)
election_results = open("election_results.txt", "w+")


for row in record:
    election_results.write(row)
    election_results.write("\n")








        
        

