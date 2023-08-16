## Model của app
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from unidecode import unidecode

import time

chrome_driver_path = './chromedriver-win64/chromedriver-win64/chromedriver.exe'
# Create ChromeOptions instance and set window size
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=800,600')

class TikiClawer:
    def __init__(self) -> object:
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        self.sleep_time = 3 # sec
        self.search_input_xpath = '//*[@id="main-header"]/div/div[1]/div[1]/div[2]/div/input'
        
    def getUrl(self, url):
        self.driver.get(url)
		