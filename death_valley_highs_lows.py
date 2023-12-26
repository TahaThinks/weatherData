import csv
from datetime import datetime
import matplotlib.pyplot as plt

# 0 STATION  1 NAME 2 DATE  3 PRCP  4 TMAX 5 TMIN  6 TOBS

filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, lows, dates = [],[],[]
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")        
        try:
            high = int(row[4])
            low = int(row[5])
        except:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# Plot high and low temperatures
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='red')



plt.show()