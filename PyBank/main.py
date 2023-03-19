import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #skip the header
    header = next(csvreader)

    #setting the variable for months
    months = []

    #setting variable for profit
    profit = []

    #setting variable for average change
    change = []

    #track the profit throughout each month
    for row in csvreader:
        #store months in array
        months.append(row[0])
        #store profit value in array
        profit.append(int(row[1]))

    #loop through the profit array
    for i in range(len(profit)-1):
        #calculate the change in monthly profit
        change.append(profit[i+1]-(profit[i]))
    #note the max profit
    maximum_gain = max(change)
    #note the max loss
    maximum_loss = min(change)
    #find the index where the max profit occurs
    max_gain_month = change.index(maximum_gain)+1
    #find the index where the max loss occurs
    max_loss_month = change.index(maximum_loss)+1
    #use the stored index to find the corresponding month
    max_month = months[max_gain_month]
    min_month = months[max_loss_month]
    


    print("Fianacial Analysis")

    print("-------------------------------------------------------")

    print(f"Total Months: {len(months)}")

    print(f"Total: ${sum(profit)}")

    print(f"Average Change: ${round(sum(change)/len(change),2)}")

    print(f"Greatest Increase in Profits: {max_month} (${maximum_gain})")

    print(f"Greatest Decrease in Profits: {min_month} (${maximum_loss})")

#export results in text file
analysis = os.path.join("Analysis", "Financial_Analysis.txt")
with open(analysis,"w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write("\n")
    file.write(f"Total Months : {len(months)}" )
    file.write("\n")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(change)/len(change),2)}")
    file.write("\n")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {max_month} (${maximum_gain})")
    file.write("\n")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {min_month} (${maximum_loss})")



