# Election_Analysis

## Overview of Election Audit

The purpose of the election audit analysis was to created an automated way to tallying and subsequently calculating totals and percentages of the provided data. I helped Tom, a Colorado board of elections employee, with analyzing the results for a U.S. congressional precinct in Colorado. I was tasked with reporting the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote. By using Python through VS code and Terminal, I was able to create a succinct, easy-to-read output that highlighted the aforementioned information. 


## Election-Audit Results


* Votes cast in congressional election: 369,711
* Breakdown of County Results
  * Jefferson: 10.5% (38,855 votes)
  * Denver: 82.8% (306,055 votes)
  * Arapahoe: 6.7% (24,801 votes)
* Denver County had the largest amount of votes 
* Breakdown of Candidate Results
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)
* Winning Candidate: Diana DeGette
  * Votes: 272,892
  * Percentage of Votes: 73.8%


## Election-Audit Summary

This script can be used for any election data. By running the script, will immidately learn the winning candidate, along with total vote count, winning county, and subsequent percentages of votes and votes for each candidate and county. 

### Modifications

One modification that might be necessary for another data set is updating the name of the file being read into the command line. See the below code for reference: 

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

If we wanted to run new election data through this script, we could keep the assigned variables, but would have the change the folder names and text file names to match what we were working with. 


It is also possible that the script might need to be modified to account for larger datasets. For example, if one wanted to use this code for the presidential election, there would be many more votes, counties, candidates, etc to account for. With that said, the script may have to be modified to account for performance testing. There are various iterations of code that can check performance of a script or program. 
