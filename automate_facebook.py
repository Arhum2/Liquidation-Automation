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

os.chdir('G:\\My Drive\\selling\\not posted')
ads = os.listdir()
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
        self.abs_path = 'G:\\My Drive\\selling\\not posted\\'
        self.post = 'https://www.facebook.com/marketplace/create/item'
        self.file_dir = c_file

        #Setting up XPATHs
        self.photo_button = "//span[text()='Add Photos']"
        self.title_button = '//*[@id=":ru:"]'
        self.title_button2 = '//*[@id=":rt:"]'
        self.title_button3 = '//*[@id=":r18:"]'
        self.price_button = '//*[@id=":rv:"]' 
        self.price_button2 = '//*[@id=":r10:"]'
        self.category_drop = '//*[@id=":r11:"]/div'
        self.category_drop2 = '//*[@id=":r12:"]/div'        
        self.category_furniture = "//span[text()='Furniture']"
        self.condition_drop = '//*[@id=":r15:"]/div'
        self.condition_drop2 = '//*[@id=":r16:"]/div'
        self.condition_new = '//*[@id=":r13:__0"]/div[1]/div/div/span'
        self.condition_new2 = '//*[@id=":r14:__0"]/div[1]'
        self.brand = '//*[@id=":r21:"]'
        self.brand2 = '//*[@id=":r22:"]'
        self.color = '//*[@id=":r1v:"]'
        self.color2 = '//*[@id=":r20:"]'
        self.description = '//*[@id=":r18:"]'
        self.description2 = '//*[@id=":r19:"]'
        self.tags = '//*[@id=":r1e:"]'
        self.tags2 = '//*[@id=":r1f:"]'
        self.done = '//span[text()="Save draft"]'

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

        #Filling photo field
        self.photo_button = self.browser.find_element(By.XPATH, (self.photo_button))
        self.photo_button.click()

        #mutating directory
        photo_directory = self.file_dir.strip('.')
        photo_directory = photo_directory + '\\photo'

        #navigating to photo folder and uploading all photos
        # pyautogui.write(self.abs_path)
        # sleep(2)
        # pyautogui.press('enter')
        sleep(2)
        pyautogui.write('G:\\My Drive\\selling\\not posted')
        sleep(2)
        pyautogui.press('enter')
        sleep(2)
        pyautogui.write(photo_directory)
        sleep(2)
        pyautogui.press('enter')
        sleep(2)
        pyautogui.moveTo(300, 200)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('enter')
        sleep(2)

        #Filling text fields py auto gui can be used here to avoid try blocks but this is easier and more spohisticated in the long run

        info = self.get_info()

        try:
            try:
                self.title_button = self.browser.find_element(By.XPATH, (self.title_button))
                self.title_button.send_keys(info['Title'])
                gate = True
        
            except NoSuchElementException:
                self.title_button = self.browser.find_element(By.XPATH, (self.title_button2))
                self.title_button.send_keys(info['Title'])
                gate = True
        
        except NoSuchElementException:
            self.title_button = self.browser.find_element(By.XPATH, (self.title_button3))
            self.title_button.send_keys(info['Title'])

            

        try:
            self.price_button = self.browser.find_element(By.XPATH, (self.price_button))
            self.price_button.send_keys(info['Price'])
        
        except NoSuchElementException:
            self.price_button = self.browser.find_element(By.XPATH, (self.price_button2))
            self.price_button.send_keys(info['Price'])

        #Drop down properties
        try:
            self.category_drop = self.browser.find_element(By.XPATH, self.category_drop).click() #reassigning selfs vars to the found element, probably not gonna be used again but good to have
            self.category_furniture = self.browser.find_element(By.XPATH, self.category_furniture).click()
        
        except NoSuchElementException:
            self.category_drop = self.browser.find_element(By.XPATH, self.category_drop2).click()
            self.category_furniture = self.browser.find_element(By.XPATH, self.category_furniture).click()

        try:
            self.condition_drop = self.browser.find_element(By.XPATH, self.condition_drop).click()
            try:
                self.condition_new = self.browser.find_element(By.XPATH, self.condition_new).click()
            except:
                self.condition_new = self.browser.find_element(By.XPATH, self.condition_new2).click()
        except:
            self.condition_drop = self.browser.find_element(By.XPATH, self.condition_drop2).click()
            try:
                self.condition_new = self.browser.find_element(By.XPATH, self.condition_new).click()
            except:
                self.condition_new = self.browser.find_element(By.XPATH, self.condition_new2).click()
                
        try:
            try:
                self.brand = self.browser.find_element(By.XPATH, self.brand)
                self.brand.send_keys(info['Brand'])
            except:
                try:
                    self.brand = self.browser.find_element(By.XPATH, self.brand2)
                    self.brand.send_keys(info['Brand'])
                
                except NoSuchElementException:
                    pass
        
        except:
            pass

        if info['Color']: #Bandaid fix
            try:
                try:
                    self.color = self.browser.find_element(By.XPATH, (self.color))
                    self.color.send_keys(info['Color'])
                
                except:
                    self.color = self.browser.find_element(By.XPATH, (self.color2))
                    self.color.send_keys(info['Color'])
            
            except NoSuchElementException:
                pass

        try:
            self.description = self.browser.find_element(By.XPATH, (self.description))
            self.description.click()
            self.description.send_keys(info['Description'])
        
        except ElementNotInteractableException: 
            self.description = self.browser.find_element(By.XPATH, (self.description2))
            self.description.click()
            self.description.send_keys(info['Description'])

        try:
            self.tags = self.browser.find_element(By.XPATH, (self.tags))
        
        except NoSuchElementException:
            self.tags = self.browser.find_element(By.XPATH, (self.tags2))

        for tag in info['Tags']:
            self.tags.send_keys(tag)
            self.tags.send_keys(Keys.ENTER)

        self.done = self.browser.find_element(By.XPATH, (self.done))
        self.done.click()

        self.browser.close()



for i in range(number_of_adds):
    curr_file = ads[i]
    testing = f'{os.curdir}\{curr_file}'
    a = Automate_add_post(f'{os.curdir}{curr_file}')
    a.automate()
    sleep(1)
    shutil.move('G:\\My Drive\\selling\\not posted\\' + curr_file, 'G:\\My Drive\\selling\\posted')
    i += 1