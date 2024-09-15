import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
from time import sleep
import pyautogui
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import shutil
from config import *

chrome_service = Service(executable_path="C:\\Program Files (x86)\\chromedriver.exe")

chrome_options = Options()
chrome_options.add_argument('--user-data-dir=C:\\Users\\pokem\\AppData\\Local\\Google\\Chrome\\User Data')
chrome_options.add_argument('--profile-directory=Profile 3')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--remote-debugging-port=9222')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-infobars')

#Navigating to selling folder
os.chdir(SELLING_FOLDER)
ads = os.listdir(SELLING_FOLDER)
number_of_adds = len(ads)

# browser = webdriver.Chrome(service=chrome_service, options=chrome_options)

#Automate class and script
class Automate_add_post:
    """
    browser: chrome browser
    post: facebook add post screen
    photo button: add photos button
    """

    def __init__(self, c_file,) -> None:

        #Setting up browser, File paths, etc
        self.browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.abs_path = NOT_POSTED_FOLDER
        self.post = 'https://www.facebook.com/marketplace/create/item'
        self.file_dir = c_file
        self.photo_button = "//span[text()='Add Photos']"
        
        self.done = '//span[text()="Save draft"]'


    # extracting info from info.txt
    def get_info(self) -> dict:

        x = self.abs_path + self.file_dir.strip('.') + '\\info.txt'
        temp = []
        result = {}

        with open(x, 'r', encoding='utf-8') as txt:
            info = txt.readlines()

            for line in info:
                temp.append(line)

        #{Tags: [list of tags]}
        for line in temp:
            curr_line = line.split(':')
            if curr_line[0] == 'Tags':
                result[curr_line[0]] = None
                x = curr_line[1].split(',')
                for item in x:
                    if result[curr_line[0]] is not None:
                        result[curr_line[0]].append(item.strip())
                    else:
                        result[curr_line[0]] = []
                        result[curr_line[0]].append(item.strip())
            else:
                result[curr_line[0]] = curr_line[1].strip()
        
        return result
    
    def automate(self):
        self.browser.get(self.post)
        sleep(3)

    #Filling text fields
        info = self.get_info()

    # === TITLE ===
        pyautogui.moveTo(50, 750)
        pyautogui.click()
        pyautogui.write(info['Title'])

    # === PRICE ===
        pyautogui.moveTo(50, 860)
        pyautogui.click()
        pyautogui.write(info['Price'])

    # === CATEGORY & CONDITION ===

        pyautogui.moveTo(50, 930)
        pyautogui.click()
        sleep(2)
        pyautogui.moveTo(50, 1100)
        sleep(2)
        pyautogui.click()
        pyautogui.moveTo(50, 1000)
        sleep(2)
        pyautogui.click()
        sleep(2)
        pyautogui.moveTo(50, 1060)
        pyautogui.click()
      
    # === DESCRIPTION ===
        pyautogui.moveTo(50, 1100)
        pyautogui.click()
        pyautogui.write(info['Description'])

        sleep(15)

        # === PHOTOS ===
        photo_directory = self.file_dir.strip('.')
        photo_directory = photo_directory + '\\photo'               
        #Filling photo field
        try:
            self.photo_button = self.browser.find_element(By.XPATH, (self.photo_button))
            self.photo_button.click()        

        except:
            pyautogui.moveTo(120, 500)
            pyautogui.click()
                
                
        #
        # navigating to photo folder and uploading all photos
        # pyautogui.write(self.abs_path)
        # sleep(2)
        # pyautogui.press('enter')
        sleep(2)
        pyautogui.write('G:\\My Drive\\selling\\not posted\\' + photo_directory)
        sleep(2)
        pyautogui.press('enter')
        sleep(2)
        # pyautogui.write(photo_directory)
        # sleep(2)
        # pyautogui.press('enter')
        sleep(2)
        pyautogui.moveTo(300, 200)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('enter')
        sleep(2)
            

        sleep(7)
        self.done = self.browser.find_element(By.XPATH, (self.done))
        self.done.click()

        self.browser.close()



for i in range(number_of_adds):
    curr_file = ads[i]
    a = Automate_add_post(f'{os.curdir}{curr_file}')
    a.automate()
    print(f'POSTED {curr_file}')
    sleep(1)
    shutil.move('G:\\My Drive\\selling\\not posted\\' + curr_file, 'G:\\My Drive\\selling\\instagram not posted\\')
    i += 1

print("TASK COMPLETED")