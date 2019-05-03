#!./P2ENV/bin/python
# Analysis

# Importing CSV module
import csv

from matplotlib import pyplot as plt
from datetime import datetime

# Get  date, highs amd lows temperature from file
filename = 'death_valley_2014.csv'
with open(filename) as f:
    # Creates a csv reader for the file given
    reader = csv.reader(f)
    # Reads the next line of the csv file with next(csvreader)
    # The line number for the next() starts with 0
    header_row = next(reader)

    # Enumerate adds index to the list supplied in argument
    # enumerated_header = enumerate(header_row)

    dates, highs, lows = [], [], []
    for row in reader:

        # Error handling
        try:
            # strptime(date, format) returns tha datetime object for python
            current_date = datetime.strptime(row[0], "%Y-%m-%d")

            # Extracting the 1st element of each list i.e. the high temp
            # Convert the strings to int
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot data
fig = plt.figure(figsize=(20, 9))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
# Filling between the graphs
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title('Daily high and low temperatures 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
