import os,sys,time,requests
from datetime import datetime
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def get_stock():
    url = "https://iboard.ssi.com.vn/"
    content = requests.get(url).text
    html = bs(content,'html.parser')

    file_html = open("D:\Coding\Web_Scrape\itemp.html",'w')
    file_html.write(str(html))
    file_html.close


get_stock()


# driver = webdriver.ChromiumEdge()
# username = "automated"
# password = "automatedautomated"
# url = "https://iboard.ssi.com.vn/"

# driver.get(url)
# time.sleep(2) # stay on the page within 2 sec
# driver.find_element("id", "id_username").send_keys(username)
# driver.find_element("id", "id_password").send_keys(password+Keys.RETURN)

# time.sleep(2) # stay on the page within 2 sec
# element = driver.find_element(by="xpath", value="/html/body/div[1]/h1[2]")
# print(element.text)
# now=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

# data_file = open(f"Data\data_file_{now}.txt",'w')
# data_file.write(element.text)
# data_file.close()

# driver.close()    