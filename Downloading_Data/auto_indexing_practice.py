import csv
from datetime import datetime
import matplotlib.pyplot as plt

# 3 different data sets to try the code on.
filename1 = 'Downloading_Data/data/sitka_weather_07-2018_simple.csv'
filename2 = 'Downloading_Data/data/death_valley_2018_simple.csv'
filename3 = 'Downloading_Data/data/Burlington__temp_wind_data_1992-2023.csv'

with open(filename3) as f:
    reader = csv.reader(f)
    header_row = next(reader)
  
    # list for program.
    tmin = []
    tmax = []
    date = []
    dates = []
    highs = []
    lows = []

    # Code to check the header for tmin and tmax and input their values into the variables
    # Display code should take different data as long as 'TMIN' and 'TMAX' are in title.
    try:
        tmin.append(header_row.index('TMIN'))
        tmax.append(header_row.index('TMAX'))
        date.append(header_row.index('DATE'))
    except ValueError:
        print(f"Missing Information required. Check Header of Data.")
    else:
        pass

    for row in reader:
        current_date = datetime.strptime(row[date[0]], '%Y-%m-%d')
        dates.append(current_date)
        highs.append(row[tmax[0]])
        lows.append(row[tmin[0]])
        

# Plot the high temperatures.
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c = 'blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha=0.1)

# Format plot.
plt.title("Daily high and low temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


