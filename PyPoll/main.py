import os
import csv
from collections import Counter

#Set path for files
csvpath1 = os.path.join("raw_data", "election_data_1.csv")
csvpath2 = os.path.join("raw_data", "election_data_2.csv")

#define counting variables
voter_count = 0
#candidates = ["Vestal", "Torres", "Seth", "Cordin"]
candidate_list = []
unique_candiates = []
vestal_count = 0
candidate_count = []

with open(csvpath1, encoding= "UTF-8", newline="") as csvfile1:
    csvreader1= csv.reader(csvfile1, delimiter=",")


    next(csvfile1)
#skip header row
#begin looping, need to count each row and output a number for number of votes
    for row in csvreader1:
        #print(row[2])
        #splitted_row = row.split(',')

        #print(splitted_row) #delimiter isn't working? Prints out in format 1759205,Matterdawn,Vestal
        #Note that the PyBank data prints out in format ['13-Apr', '957395']
        #How could I get an accurate reference to any specific column if it isn't separated?
        #-------------------------------------------------------------------------------------  
        #print(len(row)) #this prints the length of each row, I want the length of the column
        voter_count = voter_count +1
        candidate_list += [row[2]]
        #for candidate in candidate_list:
            #print(candidate)
            #if candidate == "Vestal": #takes a really long time
                #vestal_count = vestal_count+1
        #Now I want to get a count of each unique value in candidate_list
        candidate_count = Counter(candidate_list) #Counter({'Vestal': 14377, 'Torres': 13456, 'Seth': 1537, 'Cordin': 889})
        #print(candidate_count)
        
for key,value in candidate_count.items():
    #I don't have a z here, I have 
    print(key, ' ', value, " ",round((value/voter_count*100),2), "%", sep = '') #now it prints out in format "Seth 425"

winner = max(candidate_count, key=candidate_count.get)
print('Winner =', winner)


#Print out total votes

#print("vestal count:", vestal_count)
#print(unique_candiates)
print("Total votes:", voter_count)

