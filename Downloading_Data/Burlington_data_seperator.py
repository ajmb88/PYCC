from datetime import datetime
import matplotlib.pyplot as plt
import csv

filename = 'Downloading_Data/data/Burlington_percip_data_2012-2023.csv'

# Opening file and creating empty lists
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    date_index = []
    dates = []

    # Code to visualize the header.
    for value, item in enumerate(header_row):
        print(value,item)
    
    # Finding the index of the word 'DATE' and appending the value into 'date_index' list.
    date_index.append(header_row.index('DATE'))

    # getting the next line from the csv file. using the value inside of 'date_index' to find the date info.
    first_line = next(reader)
    date = first_line[date_index[0]]
    dates.append(date)
    print(date[0:7])
    print(dates)
    
    # using the last date to check against incoming dates so no duplicates are stored in the dates list
    # This list will be used to store the infomation into seperate files by month.
    for row in reader:
        last_date = dates[-1]
        new_date = row[date_index[0]]
        if new_date[0:7] in last_date[0:7]:
            print('yes')
            pass
        else:
            dates.append(new_date)
    
    print(dates)
    