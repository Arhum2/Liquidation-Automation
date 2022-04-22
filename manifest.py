import csv
import sys
from numpy import product
import pyperclip
# m16217884


# check for command line arguments

if len(sys.argv) > 1:
    file_name = ''.join(sys.argv[1:]) + ".csv"
    #print(file_name)

else:
    file_name = ''.join(pyperclip.paste()) + ".csv"
    #print(file_name)

file_path = f"D:\\download\\{file_name}"

# Read the csv

with open(f"{file_path}", 'r') as manifest:
    csv_dict_reader = csv.DictReader(manifest)
    manifestList = []
    for row in csv_dict_reader:
        item = row['Product'] + ' ' + row['Manufacturer']
        print(item)
        #print(row['Product'])
        #print(row['Manufacturer'])

