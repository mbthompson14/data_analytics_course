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
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the file
with open(file_to_load) as election_data:

    # read csv
    file_reader = csv.reader(election_data)

    # print header
    headers = next(file_reader)
    #print(headers)

    for row in file_reader:
        total_votes += 1  # increase vote count
        candidate_name = row[2]  # get candidate name
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)  # add candidate name if unique
            candidate_votes[candidate_name] = 0  # add candidate to vote tally
        candidate_votes[candidate_name] += 1  # count vote

with open (file_to_save, "w") as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)

    # calculate percentage of votes for each candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        # determine winning candidate and vote count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
