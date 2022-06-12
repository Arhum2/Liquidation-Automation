import csv
import sys
import pyperclip
from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
browser = webdriver.Chrome(PATH)
search = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'

# check for command line arguments

if len(sys.argv) > 1:
    file_name = ''.join(sys.argv[1:]) + ".csv"
    #print(file_name)

# checking for manifest name on clipboard

else:
    file_name = ''.join(pyperclip.paste()) + ".csv"
    #print(file_name)

# assigning .csv file path

file = f"D:\\download\\{file_name}"

# Read the csv and extract wanted data

with open(f"{file}", 'r') as product_list:
    csv_dict_reader = csv.DictReader(product_list)
    items = []
    for row in csv_dict_reader:
        items.append(row['Product'] + ' ' + row['Manufacturer'])

# While loop to parse the list and google search each product in a new tab

length = len(items)

i = 0
while i <= length:
    browser.get('https://www.google.com/search?q=' + f"{items[i]}")
    i = i + 1
    browser.switch_to.new_window()
    if i == items:
        break
