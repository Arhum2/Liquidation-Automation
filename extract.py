import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep
import pyautogui
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

chrome_service = Service(executable_path="C:\\Program Files (x86)\\chromedriver.exe")

chrome_options = uc.ChromeOptions()
chrome_options.add_argument('--user-data-dir=C:\\Users\\pokem\\AppData\\Local\\Google\\Chrome\\User Data')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-infobars')

#Navigating to selling folder

os.chdir('G:\\My Drive\\selling\\test')

class Extract:

    def __init__(self, link) -> None:
        self.link = link
        uc.TARGET_VERSION = 112
        self.browser = uc.Chrome(options=chrome_options)

    def extract_info(self):
        self.browser.get(self.link)
        sleep(100)

with open('G:\\My Drive\\selling\\test\\master_doc.txt', 'r') as links:
    link_list = links.readlines()

for link in link_list:
    a = Extract(link) 
    a.extract_info()