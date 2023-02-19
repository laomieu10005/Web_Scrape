import os,sys
try:
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
except:    
    os.system("pip install selenium")
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
try:
    from chromedriver_py import binary_path # this will get you the path variable
except:    
    os.system("pip install chromedriver_py")
    from chromedriver_py import binary_path # this will get you the path variable


service_object = Service(binary_path)
driver = webdriver.Chrome(service=service_object)

username = "user"
password = "password"
url = ""
data_folder = './Data'

driver.get(url)
driver.find_element("id", "login_field").send_keys("user")
driver.find_element("id", "password_field").send_keys("password")
driver.find_element("name", "commit").click()
WebDriverWait(driver=driver, timeout=20).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)
error_message = "Incorrect username or password."
errors = driver.find_elements(By.CLASS_NAME, "flash-error")

if any(error_message in e.text for e in errors): 
    print("[!] Login failed")
else:
    print("[+] Login successful")
driver.close()    