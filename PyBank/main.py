#Import csv file
import os
import csv

# from datetime import datetime

csvpath = os.path.join('Resources', 'Budget_data.csv')


# The total number of months included in the dataset

months_count = len(list(csv.reader(open(csvpath)))) - 1


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    total = 0
    data = [] 
    
   
    for row in csvreader:

        # The net total amount of "Profit/Losses" over the entire period
        total += int(row[1])
        

        # row = [Date, Profit/Losses]

        # date = datetime.strptime(row[0], '%b-%Y')
        date = row[0]
        profit_losses = int(row[1])

        data.append([date,profit_losses])
    
   
    changes =[]
    total_changes = 0
    number = len(data)


    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those change

    for i in range((number)-1):
        current_month_row = data[i]
        current_month_pl = current_month_row[1]
        

        next_month_row = data[i+1]
        next_month_pl = next_month_row[1]
        
        month = next_month_row[0]
        monthly_change = next_month_pl - current_month_pl

        total_changes += monthly_change

        changes.append([month,monthly_change])
        

    average_changes = total_changes /(number-1) 

# The greatest increase in profits (date and amount) over the entire period

    max_profit = max(changes, key=lambda item: item[1])

# The greatest decrease in profits (date and amount) over th11e entire period

    min_profit = min (changes, key=lambda item: item[1])

#Print analysis
print (" ")
print ("Financial Analysis")
print("--------------------------------------------------------")
print("Total months: " + str(months_count))
print("Total: " + str("${:,}".format(total)))
print("Average change: " + str("${:,.2f}".format(average_changes)))
print("Greatest Increase in Profits: " + str(max_profit[0]) + " (" + str("${:,}".format(max_profit[1])+ ")"))
print("Greatest Decrease in Profits: " + str(min_profit[0]) + " (" + str("${:,}".format(min_profit[1])+ ")"))

    
# Export a text file with the results

file = os.path.join('Analysis','Bank_Analysis.txt')

with open(file,'w') as f:
    
    f.write("Financial Analysis")
    f.write("\n")
    f.write("--------------------------------------------------------")
    f.write("\n")
    f.write("Total months: " + str(months_count))
    f.write("\n")
    f.write("Total: " + str("${:,}".format(total)))
    f.write("\n")
    f.write("Average change: " + str("${:,.2f}".format(average_changes)))
    f.write("\n")
    f.write("Greatest Increase in Profits: " + str(max_profit[0]) + " (" + str("${:,}".format(max_profit[1])+ ")"))
    f.write("\n")
    f.write("Greatest Decrease in Profits: " + str(min_profit[0]) + " (" + str("${:,}".format(min_profit[1])+ ")"))