from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


#windows
#And make sure we can find the profile we have just created.

#mac
#/Users/arhumshahzad/Library/Application Support/Google/Chrome/Default
options = Options()
options.page_load_strategy = 'normal'

options.add_argument("user-data-dir=/Users/arhumshahzad/Library/Application Support/Google/Chrome/User Data")

driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
driver.implicitly_wait(1000)
driver.get('https://www.youtube.com')
driver.find_element(By.ID, "input").send_keys('whats good')

