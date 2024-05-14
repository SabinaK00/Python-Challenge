import os
import csv

csvpath = os.path.join("C:\\Users\\kamalova\\Desktop\\April BootCamp\\SandBox-PrivateWork\\HomeWork\\03-Python\\Starter_Code\\PyPoll\\Resources\\election_data.csv")
file_to_output = "Election_output.txt"

# Declare
total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""




# Open File
with open('election_data.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
 
    #loop to find total votes
    for row in csvreader:

        # Find the total votes
        total_votes += 1

        candidate = row["Candidate"]
        # if statement 
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        
        candidate_votes[candidate] = candidate_votes[candidate] + 1


#title
with open(file_to_output, 'w') as txt_file:
    #create title
    election_header = (
        f"Election Results\n"
        f"---------------\n"
        f"Total votes:")
    
    txt_file.write(election_header)

    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
        
    winning_summary = (
        f"Winner: {winner}"
    )
    print(winning_summary)
    txt_file.write(winning_summary)