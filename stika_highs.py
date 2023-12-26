import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data\sitka_weather_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and high temperatures from this file.
    dates, highs = [], []
    for row in reader:
        high = int(row[5])
        highs.append(high)
        
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

# Plot the high temperatures.
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red') #X-axis is Dates & y-axis is highs

# Format Plot.
plt.title("Daily high Temperatures - 2018", fontsize=24)
plt.xlabel(" ", fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)


plt.show()