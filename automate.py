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
chrome_options.add_argument('--disable-infobars')

#Navigating to selling folder

os.chdir('G:\\My Drive\\selling\\test')
ads = os.listdir()
number_of_adds = len(ads)

#Automate class and script
class automate_add_post:
    """
    browser: chrome browser
    post: facebook add post screen
    photo button: add photos button
    """

    def __init__(self, c_file) -> None:
        self.browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.post = 'https://www.facebook.com/marketplace/create/item'
        self.photo_button = None
        self.title_button = None
        self.file_dir = c_file

    def automate(self):
        self.browser.get(self.post)
        self.photo_button = self.browser.find_element(By.XPATH, ("//span[text()='Add Photos']"))
        self.title_button.send_keys('test')
        self.photo_button.send_keys(os.getcwd() + '\\test.jpg')

for i in range(number_of_adds):
    curr_file = ads[i]
    a = automate_add_post(f'{os.curdir}\\{curr_file}')
    x = 1+1
    a.automate()

sleep(10000)

