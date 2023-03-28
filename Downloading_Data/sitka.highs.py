import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'Downloading_Data/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # Printing Header Row in an easier to read format.
    for index, column_header in enumerate(header_row):
        print(index, column_header)


    # Get dates and high temperatures from the file.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

print(highs)    


# Plot the high temperatures.
plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()
ax.plot(dates, highs, c = 'red')

# Format plot.
plt.title("Daily high temperature, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()