## Model của app
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from unidecode import unidecode
import uuid
import re
import time

chrome_driver_path = './chromedriver-win64/chromedriver-win64/chromedriver.exe'
# Create ChromeOptions instance and set window size
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--window-size=800,600')

class TikiClawer:
    def __init__(self) -> object:
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
        self.sleep_time = 3 # giây
        self.search_input_xpath = '//*[@id="main-header"]/div/div/div[2]/div[1]/div[1]/div/div/input'
        
        # Khởi tạo 
        self.name = ""
        self.brand = ""
        self.description = ""
        self.images = ""
        self.regular_price = ""
        self.discounted_price = ""
        
        
    # Lấy link
    def getUrl(self, url):
        self.driver.get(url)
        
    # Lấy link sản phẩm
    def getProductLinks(self, xpath):
        productLinks = self.driver.find_elements(By.XPATH, xpath)
        productLinks = [link.get_attribute("href") for link in productLinks]
        return productLinks
    
    # Dừng tiến trình    
    def stopProcess(self):
        self.driver.quit()
        
    # Nhập text muốn tìm
    def sendSearchInput(self, text):
        search_input = self.driver.find_element(By.XPATH, self.search_input_xpath)
        
        search_input.send_keys(text)
        search_input.send_keys(Keys.ENTER)
        time.sleep(self.sleep_time)
        
    # Trả về 1 list các sản phẩm chứa tên sản phẩm 
    def getListProduct(self, xapth):
        list = self.driver.find_elements(By.XPATH, xapth)
        list_names = [ i.text for i in list ]
        return list_names
    
    # Trả về 1 text của 1 web element
    def getProductInfo(self, xpath):
        info = self.driver.find_elements(By.XPATH, xpath)
        if info:
            info = self.driver.find_element(By.XPATH, xpath)
            return info.text
        else:
            return "Không tìm thấy sản phẩm"
    
    # Tạo ID cho sản phẩm
    def generate_item_id(self):
        timestamp = int(time.time() * 1000)
        uuid_str = str(uuid.uuid4())
        item_id = f"{timestamp}-{uuid_str}"
        return item_id
        
    
    # Lấy hình (##)
    def getImages(self):
        images = ""
        imagesEL = self.driver.find_elements(By.XPATH, '//a[contains(@data-view-id, "pdp_main_view_photo")]')
        
        for el in imagesEL:
            el.click()
            imageContainer = self.driver.find_element(By.XPATH, '//div[contains(@class, "thumbnail")]').get_attribute('innerHTML')
            if re.search(r'<picture class="webpimg-container">', imageContainer):
                images = images + re.search(r'src="([^"]+)"', imageContainer).group(1) + ", "
            self.images = images
            
    # Lấy Mô tả (##)
    def getDescription(self):
        self.description = self.driver.find_element(By.XPATH,'//div[contains(@class, "ToggleContent__View-sc-1dbmfaw-0 wyACs")]').get_attribute("innerHTML")
    
    # Lấy tên sản phẩm(??)
    def getName(self, xpath):
        pass 
    
    # Trả về 1 list prices(??)
    def getPrices(self, xpath):
        pass 
    
    # Lấy tên thương hiệu
    def getBrand(self, xpath):
        try:
            brand_name = self.driver.find_element(By.XPATH, xpath) 
            self.brand = brand_name.text
        except Exception as e:
            pass
    
    # Lấy thêm dữ liệu thì lấy
    
    
    # Lưu vào 1 list
    def appendtoTotalProduct(self, list):
        try:
            list.append({
                "ID": self.generate_item_id(),
                "Name": self.name,
                "Brand": self.brand,
                # "Description": self.description,
                "Stock": 100,
                "Sale price": self.discounted_price,
                "Regular price": self.regular_price,
                # "Images": self.image,
                })
            
            print("Added!")
        except Exception as e:
            pass
    
    # Xuất dữ liệu
    def exportData(self, path):
        pass 
    
    # Tạo file CSV
    def createCSV(self, data, path):
        pass
    
     
    
    
        
		