# election_analysis
## Overview of Election Audit
The Colorado Board of Elections has requested the following the following information from a local congressional election:
1. Total number of votes cast
2. List of candidates and the number/percentage of votes they received
3. The winning candidate based on popular vote
4. List of counties and the number of voters in each
5. The county with the highest voter turnout

## Resources
- Data source: [election_results.csv](resources/election_results.csv)
- Software: Python 3.7, Visual Studio Code 1.73.1

## Election Audit Results
- Total number of votes: 369,711
- Votes by county:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- County with the largest turnout: Denver
- Votes by candidate:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
  - Diana DeGette, who received 73.8% of the vote and 272,892 votes

## Summary
This script has automated the process of calculating election results. I propose that this script can be used for any future elections, with appropriate modifications. For example, the data source would have to be changed for each election--or I could add a feature that allows you to select which election data file to use. Additionally, the "county" variable can be changed to the appropriate election district, depending on the scale of the election (e.g., district, state).