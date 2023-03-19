import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

# Read in the CSV file
with open(election_csv,'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    header = next(csvreader)

    #setting the variable for votes
    votes = []

    #setting variables for each of the Candidates
    Stockham = 0
    DeGette = 0
    Doane = 0

    #track the profit throughout each month
    for row in csvreader:
        #store votes 
        votes.append(row[0])
        #track condidate votes
        if row[2] == "Charles Casper Stockham":
            Stockham += 1 
        elif row[2] == "Diana DeGette":
            DeGette += 1
        elif row[2] == "Raymon Anthony Doane":
            Doane += 1
    #count total votes
    total_votes = len(votes)
    #calculate the percentage of votes each candidate received
    Stockham_percentage = round(100*Stockham/total_votes,3)
    DeGette_percentage = round(100*DeGette/total_votes,3)
    Doane_percentage = round(100*Doane/total_votes,3)
    #make a dictionary for easier referencing
    candidate_votes = [Stockham, DeGette, Doane]
    candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
    votes_dict = dict(zip(candidate_votes,candidates))
    #determine the highest voting percentage
    winner_percentage = max(candidate_votes)
    #find the name associated with that percentage from the dictionary
    winner = votes_dict.get(winner_percentage)
    
    print("Fianacial Analysis")

    print("-------------------------------------------------------")

    print(f"Total Votes: {total_votes}")

    print("-------------------------------------------------------")

    print(f"Charles Casper Stockham: {Stockham_percentage}% ({Stockham})")

    print(f"Diana DeGette: {DeGette_percentage}% ({DeGette})")

    print(f"Raymon Anthony Doane: {Doane_percentage}% ({Doane})")

    print("-------------------------------------------------------")

    print(f"Winner: {winner}")

#export results in text file
analysis = os.path.join("Analysis", "Election_Analysis.txt")
with open(analysis,"w") as file:

    file.write("Election Analysis")
    file.write("\n")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("\n")
    file.write(f"Total Votes : {total_votes}" )
    file.write("\n")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {Stockham_percentage}% ({Stockham})")
    file.write("\n")
    file.write("\n")
    file.write(f"Diana DeGette: {DeGette_percentage}% ({DeGette})")
    file.write("\n")   
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {Doane_percentage}% ({Doane})")