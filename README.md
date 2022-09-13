# Election_Analysis

## Overview of Election Audit

The purpose of the election audit analysis was to created an automated way to tallying and subsequently calculating totals and percentages of the provided data. I helped Tom, a Colorado board of elections employee, with analyzing the results for a U.S. congressional precinct in Colorado. I was tasked with reporting the total number of votes cast, the total number of votes for each candidate, the percentage of votes for each candidate, and the winner of the election based on the popular vote. By using Python through VS code and Terminal, I was able to create a succinct, easy-to-read output that highlighted the aforementioned information. 


## Election-Audit Results

The code I used to get the total vote output: 
    
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]


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

This script can be used for any election data. One modification that might be necessary for another data set is updating the name of the file being read into the command line.  
