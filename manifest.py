import csv
import  sys
import pyperclip
import pandas

# check for command line arguments
#m16217884
if len(sys.argv) > 1:
    file_name = ''.join(sys.argv[1:]) + ".csv"
    #print(file_name)

else:
    file_name = ''.join(pyperclip.paste()) + ".csv"
    #print(file_name)


# remove un wanted data

data = pandas.read_csv(f"D:\download\{file_name}")
data.drop('Product', inplace=True, axis=1)
data.drop('Quantity', inplace=True, axis=1)
data.drop('Manufacturer', inplace=True, axis=1)
data.drop('UPC', inplace=True, axis=1)
data.drop('Category', inplace=True, axis=1)
data.drop('Condition', inplace=True, axis=1)
data.drop('Retail Price', inplace=True, axis=1)
data.drop('Total Retail Price', inplace=True, axis=1)


# organize .csv data into python list

with open(f"D:\download\{file_name}", "r") as manifest:
    manifestReader = csv.reader(manifest)  
    manifestList = []
    for row in manifestReader:
        if len (row) != 0:
            manifestList = manifestList + [row]
            print(manifestList)
