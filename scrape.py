import os,sys,time
from datetime import datetime
try:
    from selenium import webdriver
except:    
    os.system("pip install selenium")


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.ChromiumEdge()
username = "automated"
password = "automatedautomated"
url = "http://automated.pythonanywhere.com/login/"

driver.get(url)
time.sleep(2) # stay on the page within 2 sec
driver.find_element("id", "id_username").send_keys(username)
driver.find_element("id", "id_password").send_keys(password+Keys.RETURN)

time.sleep(2) # stay on the page within 2 sec
element = driver.find_element(by="xpath", value="/html/body/div[1]/h1[2]")
print(element.text)
now=datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

data_file = open(f"Data\data_file_{now}.txt",'w')
data_file.write(element.text)
data_file.close()

driver.close()    