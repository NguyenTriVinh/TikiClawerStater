from TikiClawer import TikiClawer
from data import *
import time 

# Const
tiki_url = "https://tiki.vn/search?q="

keywords = "balo"

tiki = TikiClawer()

tiki.getUrl(tiki_url + keywords)
links = tiki.getProductLinks(productLinksXpath)

total_products = []

time.sleep(3)

for link in links:
    # Vào chi tiết sản phẩm
    tiki.getUrl(link)

    name = tiki.getName(name_xpath)

    if name == "":
        continue
    else:
    #Lấy name 
        tiki.getName(name_xpath)
    
    # Lấy brand
        tiki.getBrand(brand_xpath)
   
    # lấy price
        tiki.getPrices(prices_xpath)

    # Lấy tỉ lệ giảm giá
        tiki.getDiscountRate(discount_rate_xpath)
    
    # Lấy số lượng sản phẩm đã bán 
        tiki.getSold()


    #Thêm vào danh sách các sản phẩm
        tiki.appendtoTotalProduct(total_products)

    # In thông tin danh sách các sản phẩm ra màn hình
    for product in total_products :   
        print('Brand: ', product['Brand'] )
        print('Name: ', product['Name'])
        print('Stock: ', product['Stock'])
        if (product['Sale price'] == "" ):
            pass
        else:
            print('Sale price: ', product['Sale price'])
            print('Discount rate: ', product['Discount rate'])
        print('Regular price: ', product['Regular price'])
        print('Sold: ', product['Sold'][7:])
        print('\n')

    
