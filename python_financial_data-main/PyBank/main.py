import os
import csv


files = os.listdir()

now = os.getcwd()

csvpath = os.path.join(now, '.vscode\python_financial_data-main\PyBank\Resources', 'budget_data.csv')
txtpath = os.path.join(now, '.vscode\python_financial_data-main\PyBank\Analysis')

month_count = 0
total_net = 0
prev_pl = 0
net_change = 0
total_change = 0
greatest_profit = 0 #This stores the largest positive number
greatest_loss = 0 #This stores the largest negative number

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

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

        #Calculate the greatest increase in profit
        if net_change > 0 and net_change > greatest_profit:
            greatest_profit = net_change
            gprofit_date = (row[0])

            #print(f"{greatest_profit} + {gprofit_date}")
        elif net_change < 0 and net_change < greatest_loss:
            greatest_loss = net_change
            gloss_date = (row[0])

            #print(f"{greatest_loss} + {gloss_date}")


#Calculate average p/l change
average_change = round(total_change / (month_count - 1), 2)
        #else:
            #prev_pl = int(row[1])
        
print("Financial Analysis")
print("-------------------------")
        
print(f"Total Months: {month_count}")
print(f"Total: {total_net}")
print(f"Average Change: {average_change}")
print(f"Greatest change in profits: {gprofit_date} (${greatest_profit})")
print(f"Greatest change in loss: {gloss_date} (${greatest_loss})")

#Export result to text file
#bankfile = open(txtpath, 'w')
os.chdir(txtpath)
bank_analysis = open("bank_analysis.txt", "w+")

record = []
record.append("Financial Analysis")
record.append("-------------------------")
record.append("Total Months: " + str(month_count))
record.append("Total: " + str(total_net))
record.append("Average Change: " + str(average_change))
record.append("Greatest change in profits: " + str(gprofit_date) + "($" + str(greatest_profit) + ")")
record.append("Greatest change in loss: " + str(gloss_date) + "($" + str(greatest_loss) + ")")

for row in record:
    bank_analysis.write(row)
    bank_analysis.write("\n")