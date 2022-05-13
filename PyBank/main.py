#import modules
import os
import csv

#set CSV file path
csvpath = os.path.join('Resources', 'budget_data.csv')

#variables
profit = 0
months = []
revenue_change = 0
prev_revenue = 0
monthly_change = []
total_change = 0
average_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

#read through CSV to pull data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip header row
    csv_header = next(csvfile)

    #add months and net total amount of profit/loss to lists
    for row in csvreader:
        months.append(row[0])
        profit += int(row[1])
        
        #also track revenue changes
        revenue_change = int(row[1]) - prev_revenue
        monthly_change.append(int(row[1]))

        #reset previous revenue variable
        prev_revenue = int(row[1])

        #determine greatest increase
        if revenue_change > greatest_increase[1]:
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row[0]

        #determine greatest decrese
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row[0]
    
#iterate through rows to determine average changes
for i in range(1, len(months)):
    revenue_change = monthly_change[i] - monthly_change[i-1]
    total_change += revenue_change

average_change = total_change / (len(months) - 1)

#print output
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(len(months)))
print("Total: " + "$" + str(profit))
print("Average change: " + "$" + str(round(average_change, 2)))
print("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")

#output to a text file
file = open("Analysis/output.txt", "w")
file.write("Financial Analysis" + "\n")
file.write("----------------------------" + "\n")
file.write("Total Months: " + str(len(months)) + "\n")
file.write("Total: " + "$" + str(profit) + "\n")
file.write("Average Change: " + "$" + str(round(average_change, 2)) + "\n")
file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")" + "\n")
file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
