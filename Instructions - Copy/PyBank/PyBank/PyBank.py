#PyBank
import os
import csv

#set CSV Path
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
outputfile = os.path.join("PyBankAnalysis", "PyBank_Written.txt")

monthchange = []
profloss = []
maxchange = ["", 0]
minchange = ["", 9999999999999999999]
monthTotal = 0
net_change = 0

#Open the CSV Path
with open(csvpath) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")

    #Line checking housekeeping
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    for row in csvreader:

        #The following 2 lines append the two columns to the variables
        monthchange.append(row[0])
        
        profloss.append(int(row[1]))

#Provides total number of months in dataset
print(len(monthchange))

#Provides total number of profits/loss. In this case, profit.
prototal = sum(profloss)

print(prototal)

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
prevNet = int(row[1])
net_change = int(row[1]) - prevNet
monthchange += [net_change]
monthchange += [row[0]]

#The greatest increase in profits (date and amount) over the entire period
if net_change > maxchange[1]:
        maxchange[0] = row[0]
        maxchange[1] = net_change

#The greatest decrease in losses (date and amount) over the entire period
if net_change < minchange[1]:
        minchange[0] = row[0]
        minchange[1] = net_change

monthAverage = sum(profloss) / len(profloss)

output = (
    f"Financial Analysis\n"
    f"----------------------------------\n"
    f"Total Months: {monthchange}\n"
    f"Total: ${prototal}\n"
    f"Average Change: ${monthAverage}"
    f"Greatest Increase in Profits:"
    f"Greatest Decrease in Profits:"
)
print(output)

#with open(outputfile, "w") as txt_file:
    #txt_file.write(output)