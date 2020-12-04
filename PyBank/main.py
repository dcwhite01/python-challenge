import os
import csv
csvfile = os.path.join("Resources","budget_data.csv")
monthcount = 0
net = 0
previous = 0
change = 0
changelist = []
biggest_increase = 0
biggest_loss = 0
profitlist = []
losslist = []
month_of_change = []
date1 = []
date2 = []
with open(csvfile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_file)
    #print("Header:" + str({csv_header}))
    for row in csv_reader:
        monthcount = monthcount + 1
        net = net + int(row[1])
        change = int(row[1]) - previous
        month_of_change.append(row[0])
        changelist.append(change)
        previous = int(row[1])
    for amount in changelist:
        if amount >= biggest_increase:
            biggest_increase = amount
            x = changelist.index(amount)
            date1.append(month_of_change[x])
        if amount <= biggest_loss:
            biggest_loss = amount
            y = changelist.index(amount)
            date2.append(month_of_change[y])
average = sum(changelist)/len(changelist)
print("Financial Analysis")
print("-----------------------------")
print("Total Months: " + str(monthcount))
print("Total: $" + str(sum(changelist)))
print("Average Change: $" + str(round(average,2)))
print("Greatest Increase in Profits: " + str(date1[len(date1)-1]) + " $" + str(biggest_increase))
print("Greatest Decrease in Profits: " + str(date2[len(date2)-1]) + " $" + str(biggest_loss))
