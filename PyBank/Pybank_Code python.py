#import modules
import os
import csv

#set path for file
budget_data_csv = os.path.join("/Users/kamalova/Desktop/April BootCamp/Homework submission/03-Python/PyBank/", "budget_data.csv")
text_path = "output_bank.txt"

#Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0

#open csv 
with open(budget_data_csv) as csvfile:  
    csvreader = csv.DictReader(csvfile)

    #Loop 
    for row in csvreader:

        #Count total
        total_months += 1

        #Calculate total revenue over the entire period
        total_revenue = total_revenue + int(row["Profit/Losses"])

        #Calculate the average change in revenue between months over the entire period
        revenue_change = float(row["Profit/Losses"]) - previous_revenue
        previous_revenue = float(row["Profit/Losses"])
        revenue_change_list.append(revenue_change)
        month_of_change.append(row["Date"])

        #The greatest increase in revenue (
        if revenue_change > greatest_increase[1]:
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row['Date']

        #The greatest decrease in revenue 
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row['Date']
    revenue_average = sum(revenue_change_list) / len(revenue_change_list)

#write changes to csv
try:
    with open(text_path, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("--------------\n")
        file.write("Total Months: %d\n" % total_months)
        file.write("Total Revenue: $%d\n" % total_revenue)
        file.write("Average Revenue Change: $%.2f\n" % revenue_average)
        file.write("Greatest Increase in Revenue: %s ($%.2f)\n" % (greatest_increase[0], greatest_increase[1]))
        file.write("Greatest Decrease in Revenue: %s ($%.2f)\n" % (greatest_decrease[0], greatest_decrease[1]))
    print("Output file '{}' has been successfully created.".format(text_path))
except Exception as e:
    print("An error occurred while writing to the output file:", e)