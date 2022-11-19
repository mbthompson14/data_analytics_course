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

# open the file
with open(file_to_load) as election_data:

    # read csv
    file_reader = csv.reader(election_data)

    # print header
    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        total_votes += 1  # increase vote count
        candidate_name = row[2]  # get candidate name
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)  # add candidate name if unique
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1


print(total_votes)
print(candidate_options)
print(candidate_votes)


# open file in write mode
with open(file_to_save, "w") as txt_file:
    pass
    # write some data
    # txt_file.write("hello")


