from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# service = Service(executable_path="C:\Users\pokem\Desktop\chromedriver.exe")
driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')

driver.get("https://www.google.com")

print(driver.title)

driver.implicitly_wait(100)