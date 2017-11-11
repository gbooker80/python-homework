import csv


# Set path for file
csvfile = open('election_data_2.csv', 'r')

reader =csv.DictReader(csvfile)
vote_total = sum(1 for row in csvfile)


print("Election Results")
print("--------------------------------")
print("Total Votes: " + str(vote_total))
print("--------------------------------")
print("--------------------------------")
print("--------------------------------")
