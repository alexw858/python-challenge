import os
import csv

#Set path for file
csvpath1 = os.path.join("raw_data", "budget_data_1.csv")
csvpath2 = os.path.join("raw_data", "budget_data_2.csv")

#open the first csv
with open(csvpath1, encoding= "UTF-8", newline="") as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter=",")

    #define variables to count unique months
    #current_month =""
    #month_name = ""
    month_count = 0
    total_revenue = 0
    revenue_change = 0
    revenue_list = []
    #need an index to store change in revenue
    change_list = []
    month = []

    #skip header row
    next(csvfile1, None)

    #begin looping through csv file
    for index, row in enumerate(csvreader1):
        #print(row)
        month += [row[0]]
        #create a list that holds all revenue values

        #candidate_count = Counter(candidate_list)

        #for month in row:
        #    print(candidate)
        revenue_list += [int(row[1])]
        revenue_list2 = revenue_list[1:]
        #create a list that hold all changes in revenue
        
        #change_list = [revenue_list[row +1]-revenue_list[row] for row in range(len(revenue_list)-1)]


        #current_month = row[0][3:6]
        #if current_month != month_name:
        month_count = month_count +1
            #print("current_month:", current_month)
            #print("month_name:", month_name)
            #month_name = current_month
        
        #current_revenue = row[1]

        total_revenue += float(row[1])
        
        #fill in change_list with revenue changes
    #print(revenue_list2)
    change_list = [b-a for a,b in zip(revenue_list, revenue_list2)]
    avg_change = float(sum(change_list))/float(len(change_list))
    print('Average Revenue Change =', avg_change)
    #calculate average change ()
    



#Print the output
    #print("rev list len:", len(revenue_list))
    #print("rev list2 len:", len(revenue_list2))
    print("Month count:", month_count)
    print("Total revenue:", total_revenue)
    max_change = max(change_list)
    #Where the greatest increase occurs:
    index_max = change_list.index(max_change)
    print("Greatest increase in revenue:", max_change)
    #print("Greatest increase in revenue:", row[index_max]) #how to index the position in my original list?
    min_change = min(change_list)
    print("Greatest decrease in revenue:", min_change)