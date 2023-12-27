import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/skita_weather_2018_simple.csv'

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

