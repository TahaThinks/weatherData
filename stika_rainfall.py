import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename1 = 'data/sitka_weather_2018_simple.csv'
filename2 = 'data/death_valley_2018_simple.csv'

# Extracting Rainfall & Dates for Skita:
with open(filename1) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    skita_rainfall, skita_dates = [],[]
    for row in reader:
        daily_rain = float(row[3])
        skita_rainfall.append(daily_rain)

        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        skita_dates.append(current_date)

# Extracting Rainfall & Dates for DeathValley
with open(filename2) as f:
    reader = csv.reader(filename2)
    header_row = next(reader)

    dv_rainfall, dv_dates = [],[]
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        dv_dates.append(current_date)
        try:
            daily_rain = float(row[3])
        except:
            print(f"Data not available for Date: {current_date}")
        else:
            dv_rainfall.append(daily_rain)
            dv_dates.append(current_date)


# Plot the Rainfall with respect to the Date
plt.style.use('seaborn-v0_8-bright')
fig, ax = plt.subplots()
ax.plot(skita_dates, skita_rainfall, c="dodgerblue")


# Format Plot:
plt.title("Daily Rainfall in Stika - 2018", fontsize=24)
plt.xlabel(" ", fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
