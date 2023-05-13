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
chrome_options.add_argument('--profile-directory=Profile 3')
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
        self.title = 'h1'
        self.description_button = '//*[@id="CollapseToggle-2"]'
        self.product_overview = '//*[@id="CollapsePanel-2"]/div/div/div'
        self.description = None
        self.features = '//*[@id="CollapsePanel-2"]/div/div/div/div[2]/div/ul'
        self.dimensions_button = '//*[@id="CollapseToggle-3"]'
        self.dimensions = '//*[@id="Pres_list_keyval::0"]/h4'
        self.browser = uc.Chrome(options=chrome_options, version_main=112)
        self.browser.get(self.link)

        self.images = '/html/body/div[4]/div/main/div/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div/div[3]/ul/li[1]/div/div/div/div'


    # def make_dir(self):
    #     curr_dir = os.getcwd()
    #     wrong_lst = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    #     title = self.title.strip()

    #     for char in title:
    #         if char in wrong_lst:
    #             title = title.strip(char)

    #     dir_path = f'{curr_dir}\\{title}'

    #     os.makedirs(title)
    #     os.chdir(dir_path)
    
    # def extract_info(self):
    #     # self.browser.get(self.link)
    #     self.title = self.browser.find_element(By.TAG_NAME, self.title)
    #     self.title = self.title._parent.title

    #     self.description_button = self.browser.find_element(By.XPATH, self.description_button)
    #     self.description_button.click()
        
    #     self.product_overview = self.browser.find_element(By.XPATH, self.product_overview)
    #     self.description = self.product_overview.text

    #     self.features = self.browser.find_element(By.XPATH, self.features)
    #     self.features = self.features.text

    #     self.dimensions_button = self.browser.find_element(By.XPATH, self.dimensions_button)
    #     self.dimensions_button.click()

    #     self.dimensions = self.browser.find_element(By.XPATH, self.dimensions)
    #     self.dimensions = self.dimensions.text

    #     self.make_dir()

    #     result = open("info.txt", 'x')
    #     result.write(f'Title: {self.title}\n')
    #     result.write(f'Description: {self.description}\n')
    #     result.write('Brand: Wayfair\n')
    #     result.write('Tags: Wayfair, Furniture, Bed, Matress, Homedecor, Rustic, Boho, Decor, Home, Interior, Sofa, Daybed, Sale, Vintage, Chair, Stool, Velvet, Luxury, Kitchen, Bedroom\n')
    #     result.close

    def extract_pics(self):
        self.images = self.browser.find_element(By.CLASS_NAME, self.images)
        x = self.images.get_attribute('src')

with open('G:\\My Drive\\selling\\test\\master_doc.txt', 'r') as links:
    link_list = links.readlines()

for link in link_list:
    a = Extract(link)
    # a.extract_info()
    a.extract_pics()