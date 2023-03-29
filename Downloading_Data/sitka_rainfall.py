# All imports.
import csv
from datetime import datetime
from plotly.graph_objs import Bar, Layout
from plotly import offline

# Naming the file and opening to read data.
filename = 'Downloading_Data/data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Initializing lists to store precipitation and dates
    prcp = []
    dates = []

    # Reading the data, converting the date, and assinging values to the lists.
    for row in reader:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        number = float(row[3])
        prcp.append(number)
        dates.append(date)

# Visualize the results.
x_value = dates
data = (Bar(x = x_value, y = prcp))

x_axis_config = {'title': 'Dates'}
y_axis_config = {'title': 'Amount of precipitation in cm?'}
my_layout = Layout(title="Amount of average rainfall in Sitka in 2018", xaxis = x_axis_config,
                    yaxis = y_axis_config)
offline.plot({'data' : data, 'layout' : my_layout}, filename= 'Sitka_2018.html')


print(header_row)
print(prcp)