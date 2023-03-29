import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Sitka weather data
filename = 'Downloading_Data/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Printing Header Row in an easier to read format.
    for index, column_header in enumerate(header_row):
        print(index, column_header)


    # Get dates, and high and low temperatures from the file.
    sitka_dates, sitka_highs, sitka_lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        sitka_dates.append(current_date)
        sitka_highs.append(high)
        sitka_lows.append(low)


# Death valley weather data
filename = 'Downloading_Data/data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from the file.
    death_dates, death_highs, death_lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        # Error handling code for when full data is collected
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing Data for {current_date}")
        else:
            # Only appending the dates that match sitka weather data.
            if current_date in sitka_dates:
                death_dates.append(current_date)
                death_highs.append(high)
                death_lows.append(low)

# Plot the temperature differences.
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(sitka_dates, sitka_highs, c='red', alpha=0.5)
ax.plot(sitka_dates, death_highs, c = 'blue', alpha=0.5)
plt.fill_between(sitka_dates, sitka_highs, death_highs, facecolor = 'blue', alpha=0.1)

# Format plot.
plt.title("Sitka vs Death Valley High Temps, July, 2018.", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
      

print(f" Death valley dates: {death_dates}\n")
print(f"Sitka dates: {sitka_dates}")