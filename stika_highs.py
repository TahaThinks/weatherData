import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data\sitka_weather_07-2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get high temperature from this file
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# Plot the high temperatures.
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(highs, c='red')

# Format Plot.
plt.title("Daily high Temperatures, july 2018", fontsize=24)
plt.xlabel(" ", fontsize=14)
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()