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
# Open the election results and read the file.
#with open(file_to_load) as election_data:

    # Print the file object.
     #print(election_data)

#Create a filename variable to a direct or indirect path to the file ( save the file to a path)

file_to_save = os.path.join("analysis", "election_analysis.txt")

#Use the open statement to open results and read the file.
with open(file_to_load) as election_data:

        #To do: read and analyze the data here
         # Read the file object with the reader function.
        file_reader = csv.reader(election_data)
        headers = next(file_reader)
        print(headers)

        # Print each row in the CSV file.
        #for row in file_reader:
                #print(row)


# Write some data to the file.
       # txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

