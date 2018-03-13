# Modules
import os
import csv

total_vote = []
candidates = []
candidates_set = set(candidates)

csvpath = os.path.join("raw_data", "election_data_1.csv")
outputTXT = os.path.join("raw_data", "election1.txt" )

with open(csvpath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  next(csvreader, None)

  for row in csvfile:
    total_vote.append(row[0])
    candidates.append(row[2])
    candidates_set.add(str(row[2]))
    
print(candidates_set)
print("Election Results")
print("------------------------------")
print("Total Votes:" + str(len(total_vote)))
print("------------------------------")

