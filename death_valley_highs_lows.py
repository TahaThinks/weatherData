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
        high = int(row[4])
        highs.append(high)

        low = int(row[5])
        lows.append(lows)

        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dates.append(current_date)
