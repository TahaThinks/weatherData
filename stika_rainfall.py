import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'

# Extracting Rainfall & Dates:

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    rainfall, dates = [],[]
    for row in reader:
        daily_rain = float(row[3])
        rainfall.append(daily_rain)

        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)

# Plot the Rainfall with respect to the Date
plt.style.use('seaborn-v0_8-bright')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c="dodgerblue")


plt.show()
