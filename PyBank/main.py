# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


files = os.listdir()

now = os.getcwd()

#print(now)

#for file in files:
#print(os.path.join(now,'.vscode\python_financial_data-main\PyBank\Resources'))


csvpath = os.path.join(now, '.vscode\python_financial_data-main\PyBank\Resources', 'budget_data.csv')

month_count = 0
total_net = 0
prev_pl = 0
net_change = 0
total_change = 0
greatest_profit = 0 #This stores the largest positive number
greatest_loss = 0 #This stores the largest negative number

with open(csvpath) as csvfile:
     # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

      # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
   
        print(row) 
        #Calculate the total period number
        month_count = month_count + 1
        
        #Calculate the total Profit/Loss in all periods
        total_net = total_net + int(row[1])
        
        #Calculate the change in Profit/Loss over each period and the accumulated change
        if month_count > 1:
            net_change = int(row[1]) - prev_pl
            total_change = total_change + net_change
        prev_pl = int(row[1])

        #else:
            #prev_pl = int(row[1])
        

        print(month_count)
        print(total_net)

