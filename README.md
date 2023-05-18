# python_challenge

# PayPoll

## Introduction

This script is a solution to analyzing poll data from an election. The objective is to create a Python script that reads in a CSV file containing data like "Voter ID", "County", and "Candidate" and performs analysis on this data to extract meaningful insights.

## Code Explanation
-The script begins by importing the `csv` module, which provides functionality for reading and writing CSV files. It then initializes variables to store the total number of votes cast, the number of votes won by each candidate, and a list of candidates who received votes.

-The script reads in the election data from the CSV file using the `open()` function in combination with the `csv.reader()` method. These built-in Python functions allows the program to read in a CSV file row by row.

-For each row of election data, the script first increments the total vote count, which is stored in the `count_votes` variable. The script then checks whether the candidate who received the vote is already in the `vote_counts` dictionary. If the candidate is already in the dictionary, the program increments the existing vote count for that candidate. If the candidate is new to the dictionary, the program adds the candidate to the dictionary with an initial vote count of 1.

-The script also keeps a separate list of all the candidates who received votes. This list is used later to loop through the `vote_counts` dictionary to output the results.

-After the raw data has been processed, the script calculates the percentage of votes each candidate received by dividing the candidate's vote count by the total vote count and multiplying the result by 100. This calculation is done for each candidate in the `vote_counts` dictionary and the results are stored in a new dictionary called `percentage_votes`.

-Finally, the script uses a max function to determine the candidate who won the election based on the popular vote. The `max()` function returns the key with the highest value (vote count) in the `vote_counts` dictionary.

-The results are then formatted as a string, printed to the console, and written to a text file called `election_results.txt` using the `write` method.

# references
https://github.com/Angienoelhaverly/Election_Analysis/blob/main/PyPoll.py
https://docs.python.org/3/
https://docs.python.org/3/library/csv.html

# PayBank

## Introduction

The "budget_analysis.py" script is a Python program that analyzes financial data from a csv file and calculates various statistics such as the total number of months, the net total amount of profit/losses, the average monthly change in profit/losses, and the greatest increase and decrease in profits over the entire period. The analysis results are printed to the console in a clear and organized format. This script is particularly useful for businesses or individuals who want to gain insights into their financial data.

## Code Explanation

The "budget_analysis.py" script performs the following steps:

- Imports the "csv" module, which allows us to read and write csv files in Python.
- Defines the file path of the csv file we want to analyze.
- Defines three empty lists to store the data from the csv file.
- Reads the csv file and stores the data in the three lists.
- Calculates the total number of months in the dataset.
- Calculates the net total amount of profit/losses over the entire period.
- Calculates the changes in profit/losses over the entire period and stores them in a separate list.
- Calculates the average monthly change in profit/losses.
- Finds the greatest increase and decrease in profits over the entire period and the dates on which they occurred.
- Prints out the analysis results in a clear and organized format using f-strings and print the results in .txt file. 

## References

The following references were used in creating this script:

- https://github.com/joathanner/Python-Project/blob/master/main.py
- Python documentation: https://www.python.org/doc/
- Python csv module documentation: https://docs.python.org/3/library/csv.html
- GeeksforGeeks Python tutorials: https://www.geeksforgeeks.org/python-programming-language/
- Real Python tutorials: https://realpython.com/


