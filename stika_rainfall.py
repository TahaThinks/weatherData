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
        stika_daily_rain = float(row[3])
        skita_rainfall.append(stika_daily_rain)

        stika_current_date = datetime.strptime(row[2], "%Y-%m-%d")
        skita_dates.append(stika_current_date)

# Extracting Rainfall & Dates for DeathValley
with open(filename2) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dv_rainfall, dv_dates = [],[]
    for row in reader:
        try:
            dv_current_date = datetime.strptime(row[2], "%Y-%m-%d")
            dv_daily_rain = float(row[3])
        except:
            print(f"Data not available for Date:{dv_current_date}")
        else:
            dv_rainfall.append(dv_daily_rain)
            dv_dates.append(dv_current_date)


# Plot the Rainfall with respect to the Date
plt.style.use('seaborn-v0_8-bright')
fig, ax = plt.subplots()
ax.plot(skita_dates, skita_rainfall, c="dodgerblue")
ax.plot(dv_dates, dv_rainfall, c="darkviolet") 


# Format Plot:
plt.title("Daily Rainfall in Stika vs Death Valley - 2018", fontsize=24)
plt.xlabel(" ", fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
