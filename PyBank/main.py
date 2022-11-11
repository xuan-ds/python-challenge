
# create file path
import os
# use csv Module for reading CSV files
import csv

# select CSV file 
csvpath = os.path.join('/Users/xuandi/Desktop/python-challenge/PyBank/Resources/budget_data.csv')

# open CSV file
with open(csvpath) as csvfile:

    # read CSV file 
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    # skip the header 
    next(csvreader)
 
    # create a variables with a list of the profit loss data.
    profit_loss_list = []

    # create a varaible with a data list
    data_list = []

    # create a variable with a list contains the changes in profit/losses
    change_list = []

    # loop through the row and seprate two data sets into two lists
    for row in csvreader:
        profit_loss_list.append(int(row[1]))
        data_list.append(row[0])

# loop through the profist/losses list
for i in range(1,len(profit_loss_list)):
    change_list.append(profit_loss_list[i] - profit_loss_list [i-1])

total_month = len (profit_loss_list)
total_profit_loss = sum(profit_loss_list)
average_change = (profit_loss_list[-1] - profit_loss_list[0]) / (total_month - 1)

gi_profit = max(change_list)
gd_profit = min(change_list)

gi_profit_index = change_list.index(gi_profit)
gd_profit_index = change_list.index(gd_profit)
gi_date = data_list[gi_profit_index+1]
gd_date = data_list[gd_profit_index+1]

#print out the results:
print("Financial Analysis")
print("-----------------------------")
print("Total Months:",total_month)
print ("Total: " + "$" + str(total_profit_loss))
print("Average Change: " + "$" + str(float("{:.2f}".format(average_change))))
print("Greatest Increase in Profits: " + str(gi_date) + " ($" + str(gi_profit) + ")")
print("Greatest Decrease in Profits: " + str(gd_date) + " ($" + str(gd_profit) + ")")