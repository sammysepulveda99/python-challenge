#Import the os module to create file paths across operating systems
import os
#Module for reading CSV
import csv
csvpath = os.path.join('PyBank','Resources',"budget_data.csv")

#Lists to store data
total_months = 0
net_totalprofit_loss= 0
value = 0
changes_profit_loss= 0
date = []
profit = []


#Improved reading with CSV module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
 
#Read the header row first
    csv_header= next(csvreader)
    firstrow= next(csvreader)
    total_months +=1
    net_totalprofit_loss += int(firstrow[1])
    value = int(firstrow[1])
#Read each row of data after the header
    for row in csvreader:
 #Add the dates
        date.append(row[0])

 #Total number of months
        total_months += 1

 #Calculating  changes in profit and loss
        amount = int(row[1])-value
        profit.append(amount)
        value = int(row[1])

#Net amount of profit loss
        net_totalprofit_loss= net_totalprofit_loss + int(row[1])

#Average change in profit loss
        changes_profit_loss= sum(profit)/len(profit)

#Add greatest increase in profit
        greatest_increaseprofit = max(profit)
        greatest_index = profit.index(greatest_increaseprofit)
#Add date to greatest increase
        greatest_date= date[greatest_index]

#Add greatest decrease in profit
        greatest_decreaseprofit = min(profit)
        lowest_index = profit.index(greatest_decreaseprofit)
#Add date to greatest decrease
        lowest_date= date[lowest_index]


#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(net_totalprofit_loss)}")
print(f"Average Change: ${str(round(changes_profit_loss,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increaseprofit)})")
print(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_decreaseprofit)})")

#Exporing to a .txt file

output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(net_totalprofit_loss)}")
line5 = str(f"Average Change: ${str(round(changes_profit_loss,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increaseprofit)})")
line7 = str(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_decreaseprofit)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))






