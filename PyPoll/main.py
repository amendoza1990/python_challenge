#Import csv file
import os
import csv

csvpath = os.path.join('Resources', 'Election_data.csv')

# The total number of votes cast
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader =csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total = 0

    data = []

    #candidate_list = [candidate, percentage, total_votes]

    candidate_list =[]
    
    for row in csvreader:

      total += 1

      candidate = str(row[2])

      data.append(candidate)
        

# A complete list of candidates who received votes

for c in data:

   if c not in candidate_list:
    candidate_list.append(c)

percentage = []
total_votes = []



for e in range(len(candidate_list)):


# The total number of votes each candidate won

 votes = (data.count(candidate_list[e]))
 total_votes.append(votes)

# The percentage of votes each candidate won
 per = votes / total
 percentage.append(per)


final_list = list(zip(candidate_list,percentage,total_votes))

# The winner of the election based on popular vote.

winner = int(max(total_votes))

winner_name=[]

for w in final_list:
    
    if w[2]== winner:
     winner_name.append(w[0])
        

#Print results
print (" ")
print ("Election Results")
print("-----------------------------------------------")
print ("Total votes: " + str(total))
print("-----------------------------------------------")

for p in final_list:
    print (str(p[0]) + ": " + str("{:.0%}".format(p[1])) + " (" + str(p[2]) + ")")

print("-----------------------------------------------")
print ("Winner: " + str(winner_name[0]))
print("-----------------------------------------------")

# Export a text file with the results

file = os.path.join('Analysis','Poll_Analysis.txt')

with open(file,'w') as f:

    f.write("Election Results")
    f.write("\n")
    f.write("-----------------------------------------------")
    f.write("\n")
    f.write("Total votes: " + str(total))
    f.write("\n")
    f.write("-----------------------------------------------")
    f.write("\n")

    for p in final_list:
        f.write (str(p[0]) + ": " + str("{:.0%}".format(p[1])) + " (" + str(p[2]) + ")")
        f.write("\n")

    f.write("-----------------------------------------------")
    f.write("\n")
    f.write("Winner: " + str(winner_name[0]))
    f.write("\n")
    f.write("-----------------------------------------------")