import csv
import sys
import pyperclip
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import requests
import os

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
path = os.getenv('PATH')
# file_name = 'm16327655' test
browser = webdriver.Chrome(path)
# check for command line arguments

if len(sys.argv) > 1:

    file_name = ''.join(sys.argv[1:]) + ".csv"

# checking for manifest name on clipboard

else:
    file_name = ''.join(pyperclip.paste()) + ".csv"

# assigning .csv file path

file = f"D:\download\{file_name}"

# Read the csv and extract wanted data

with open(f"{file}", 'r') as product_list:
    csv_dict_reader = csv.DictReader(product_list)
    items = [] 
    upc = []
    for row in csv_dict_reader:
        items.append(row['Product'] + ' ' + row['Manufacturer'])
        upc.append(row['UPC'])

# While loop to parse the list and google search each product in a new tab
upc_not_found = []

i = 0
while i < (len(items)):
    current_upc = upc[i]
    browser.get('https://www.google.com/search?q=' + f"{items[i]}")
    response = requests.get(f"https://api.upcitemdb.com/prod/trial/lookup?upc={current_upc}")
    sleep(1)
    data = response.json()

    if data['code'] == "INVALID_QUERY" or data['code'] == "INVALID_UPC" or data['total'] == 0:
        upc_not_found.append(items[i])
    
    else:
        browser.switch_to.new_window()
        browser.get('https://www.facebook.com/')
        email_field = browser.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
        password_field = browser.find_element(By.XPATH, '//*[@id="pass"]').send_keys(password)
        log_in = browser.find_element(By.NAME, "login")
        log_in.click()
        mktp_button = browser.find_element_by_xpath('//a[@href="/marketplace/?ref=app_tab"]').click()
        new_listing = browser.find_element_by_xpath('//a[@href="/marketplace/create/"]').click()

        sleep(300)

    browser.switch_to.new_window()
    
    
    i += 1
    if i == items:
        break

