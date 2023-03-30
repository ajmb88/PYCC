from datetime import datetime
import matplotlib.pyplot as plt
import csv

filename = 'Downloading_Data/data/Burlington_percip_data_2012-2023.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for value, item in enumerate(header_row):
        print(value,item)
