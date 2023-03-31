from datetime import datetime
import matplotlib.pyplot as plt
import csv

filename = 'Downloading_Data/data/Burlington__temp_wind_data_1992-2023.csv'
date_index = []
dates = []

# Opening file and creating empty lists
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    # Code to visualize the header.
    for value, item in enumerate(header_row):
        print(value,item)
    
    # Finding the index of the word 'DATE' and appending the value into 'date_index' list.
    date_index.append(header_row.index('DATE'))

    # getting the next line from the csv file. using the value inside of 'date_index' to find the date info.
    first_line = next(reader)
    date = first_line[date_index[0]]
    dates.append(date)
    print(date[0:4])
    print(dates)
    
    # using the last date to check against incoming dates so no duplicates are stored in the dates list
    # This list will be used to store the infomation into seperate files by month.
    for row in reader:
        last_date = dates[-1]
        new_date = row[date_index[0]]
        if new_date[0:4] in last_date[0:4]:
            print('yes')
            pass
        else:
            dates.append(new_date)
    
print(dates)




# Date were working with for the moment is 'working_date'. Its the last dates from dates list.
for date in dates:
    working_date = dates.pop()
    
    # Opening the new filename in write mode and putting the data year in title.
    with open(f"Downloading_Data/data/Burlington_Temperature_data/Burlington_Weather_Data_Year_{working_date}.csv", 'w') as g:
        writer = csv.writer(g)
        writer.writerow(header_row)   

        # Opening  the data file taking out the header
        with open(filename) as f:
            reader2 = csv.reader(f)
            header_row = next(reader2)

            # go through data until the selected date matches the date in file. Copy all info into new file.
            for next_row in reader2:
               
                data_date = next_row[date_index[0]]
                if working_date[0:4] in data_date[0:4]:
                   writer.writerow(next_row)