from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'normal'
#windows
#And make sure we can find the profile we have just created.

#mac
#/Users/arhumshahzad/Library/Application Support/Google/Chrome/Default
options.add_argument("user-data-dir=/Users/arhumshahzad/Library/Application Support/Google/Chrome/User Data")

driver = webdriver.Chrome(options=options)
driver.get('https://www.youtube.com')