import csv
import os

budget_data = "D:/Data analytics bootcamp/week3/module_3_challenge/python_challenge/PayBank/resources/budget_data.csv"

# Initialize variables
total_months = 0
total_profit_losses = 0
average_change = 0

# Initialize variables for the changes in profit/losses
previous_profit_losses = 0
current_profit_losses = 0
profit_losses_change = 0
changes_profit_losses = []

# Initialize variables for greatest increase and decrease in profits, and their respective dates
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""

# Read CSV file
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader) # Skip header row

    # Loop through each row in the CSV file
    for row in csv_reader:
        # Increment total months
        total_months += 1
        
        # Calculate the net total amount of Profit/Losses
        total_profit_losses += int(row[1])
        
        # Calculate the changes in Profit/Losses
        current_profit_losses = int(row[1])
        if previous_profit_losses != 0:
            profit_losses_change = current_profit_losses - previous_profit_losses
            changes_profit_losses.append(profit_losses_change)
        
        # Calculate the greatest increase in profits and the respective month
        if profit_losses_change > greatest_increase:
            greatest_increase = profit_losses_change
            greatest_increase_month = row[0]
        
        # Calculate the greatest decrease in profits and the respective month
        if profit_losses_change < greatest_decrease:
            greatest_decrease = profit_losses_change
            greatest_decrease_month = row[0]
        
        # Set previous_profit_losses for the next loop iteration
        previous_profit_losses = current_profit_losses

# Calculate the average change in Profit/Losses
average_change = round(sum(changes_profit_losses) / len(changes_profit_losses), 2)

# Print financial analysis
print("Financial Analysis")
print("-" * 30)
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Write financial analysis to a text file and save in analysis folder
output_path = os.path.join("D:/Data analytics bootcamp/week3/module_3_challenge/python_challenge/PayBank/analysis", "financial_analysis.txt")
with open(output_path, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("-" * 30 + "\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_profit_losses}\n")
    txt_file.write(f"Average Change: ${average_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

print(f"Financial analysis has been written to {output_path}.")