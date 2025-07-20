# Data to retrieve:
# 1) total number of votes cast
# 2) complete list of candidates who received votes
# 3) percentage of votes each candidate won
# 4) total number of votes each candidate won
# 5) the winner of the election based on popular vote

# import dependencies
import csv
import os

# assign data file path to variable
file_to_load = os.path.join('resources', 'election_results.csv')

# assign output file path to variable
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# initialize vote counter
total_votes = 0

# candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# county list and county votes
county_list = []
county_votes = {}

# track the winning candidate
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# track the largest county turnout
winning_county = ""
winning_county_count = 0

# open the file
with open(file_to_load) as election_data:

    # read csv
    file_reader = csv.reader(election_data)

    # read header
    headers = next(file_reader)

    # for each row in csv
    for row in file_reader:
        total_votes += 1  # increase vote count
        candidate_name = row[2]  # get candidate name
        county_name = row[1]  # get county name
        if candidate_name not in candidate_options:  # if candidate name is unique:
            candidate_options.append(candidate_name)  # add candidate name to list
            candidate_votes[candidate_name] = 0  # add candidate to dictionary
        candidate_votes[candidate_name] += 1  # count candidate vote
        if county_name not in county_list: # if county name is unique:
            county_list.append(county_name) # add county name to list
            county_votes[county_name] = 0 # add county name to dictionary
        county_votes[county_name] += 1 # count candidate vote

# save results to text file
with open (file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # loop thru county dictionary to print results
    for county_name in county_votes:
        c_votes = county_votes[county_name]  # get county votes
        c_votes_percentage = float(c_votes) / float(total_votes) * 100  # calculate percentage
        county_results = (f"{county_name}: {c_votes_percentage:.1f}% ({c_votes:,})\n")
        print(county_results)

        # save county votes to text file
        txt_file.write(county_results)

        # determine winning county
        if (c_votes > winning_county_count):
            winning_county_count = c_votes
            winning_county = county_name
    
    # print county with largest turnout
    winning_county_results = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n"
    )
    print(winning_county_results)

    # save winning county to text file
    txt_file.write(winning_county_results)

    # calculate percentage of votes for each candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # print candidate results
        print(candidate_results)

        # save candidate reuslts to text file
        txt_file.write(candidate_results)

        # determine winning candidate and vote count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # print winnning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
