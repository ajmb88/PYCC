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
    for value, item in enumerate(header_row):
        print(value,item)
    
    # Finding the index of the word 'DATE' and appending the value into 'date_index' list.
    date_index.append(header_row.index('DATE'))

    # getting the next line from the csv file. using the value inside of 'date_index' to convert date into string.
    first_line = next(reader)
    first_date = datetime.strptime(first_line[date_index[0]], '%Y-%m-%d')
    # test print
    print(first_date)

    # adding the first date to the list then appening with every other date