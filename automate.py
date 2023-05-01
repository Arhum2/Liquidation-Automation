import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep

chrome_service = Service(executable_path="C:\\Program Files (x86)\\chromedriver.exe")

chrome_options = Options()
chrome_options.add_argument('--user-data-dir=C:\\Users\\pokem\\AppData\\Local\\Google\\Chrome\\User Data')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-infobars')


browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
browser.get('https://www.facebook.com/marketplace/create/item')
sleep(5)
browser.find_element(By.XPATH, ("//span[text()='Add Photos']")).click()
sleep(5)

sleep(10000)

