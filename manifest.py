import csv
import  sys
import pyperclip

# check for command line arguments
#m16217884

if len(sys.argv) > 1:
    file_name = ''.join(sys.argv[1:]) + ".csv"
    #print(file_name)

else:
    file_name = ''.join(pyperclip.paste()) + ".csv"
    #print(file_name)

with open(f"D:\download\{file_name}", "r") as manifest:
    manifestReader = csv.reader(manifest)
    manifestList = []
    for row in manifestReader:
        if len (row) != 0:
            manifestList = manifestList + [row]
            print(manifestList)
