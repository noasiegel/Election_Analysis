# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A completel list of candidates who recieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path (load a fule from a path)
file_to_load = os.path.join("Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file ( save the file to a path)

file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter
total_votes = 0 

#Candidate options
#candidate_options = ['Raymond Anthony Doane', 'Diana Degette', 'Charles Casper Stockham' ]
candidate_options = [ ]

# 1. Delcare the empty dictionary to link a vote count to a candidate (remember dict uses curly brackets)

candidate_votes = {}

# Winning candidate and winning count tracker

winning_candidate = ''
winning_count = 0
winning_percentage = 0
#Use the open statement to open results and read the file.
with open(file_to_load) as election_data:

         # Read the file object with the reader function.
        file_reader = csv.reader(election_data)

        #read header row
        headers = next(file_reader)
        #print(headers)

        #Print each row in the CSV file.
        for row in file_reader:
                #2. Add the total vote count
                total_votes +=1

        # Print the candidate name from each row - TAB THIS OR ELSE IT WONT BE IN THE FOR LOOP
                candidate_name = row[2]

        #If the candidate does not match any existing candidate...
                if candidate_name not in candidate_options:

                #add it to the list of candidates 
                        candidate_options.append(candidate_name)

                #2. begin tracking that candidate's vote count
                        candidate_votes[candidate_name] = 0

                #3. Add a vote to that candidate's count - align with if statement but inside for loop
                candidate_votes[candidate_name] +=1

                

# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
        for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
                votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
                vote_percentage = float(votes) / float(total_votes) * 100


                if (votes > winning_count) and (vote_percentage > winning_percentage):
                        #if true, then set winning_count = votes and winning_percet = vote_percent
                        winning_count = votes
                        winning_percentage = vote_percentage
                        winning_candidate = candidate_name
    # 4. Print the candidate name and percentage of votes.
                #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
                print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        winning_candidate_summary = (
                f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_count:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"-------------------------\n")
        print(winning_candidate_summary)
                
        #3. Print the total votes.       
        #print(candidate_votes)


# Write some data to the file.
       # txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

