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
        print(f"Row {i}: {row}")
        if i > 5:
            break
