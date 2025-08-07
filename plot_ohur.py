"""
Ohio Unemployment Rate Visualization
Jeroldine Oakley [author]
This program reads unemployment data from OHRU.csv
and plots it by year.
08/06/2025
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv

# Produce header for viewing using enumerate() method
with open('OHUR.csv', 'r') as file:
    reader = csv.reader(file)

    # Enumerate through file and print first 5 rows to
    # get a general idea of the rows and columns
    for i, row in enumerate(reader):
        # Print the row number and the row content
        print(f"Row {i}: {row}")
        if i > 5:
            break

# Read the data from the CSV file and drop any rows with missing values
data = pd.read_csv('OHUR.csv').dropna()

# Set up columns for the DataFrame
data.columns = ['Year', 'Unemployment Rate']

# Convert the 'Year' column to datetime format
data['Year'] = pd.to_datetime(data['Year']).dt.year

# Set the 'Year' column as the index
data.set_index('Year', inplace=True)

# View first 5 of DataFrame to check data
print(data.head())

# Check data info to see if there are still missing/null values
print(data.info())
