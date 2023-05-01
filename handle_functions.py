import os
import sys,time
import subprocess
from threading import Thread

# =================inspect======================#
from inspect import currentframe, getframeinfo
# debug__(getframeinfo(currentframe()))

try:
    from selenium import webdriver
except:
    os.system("pip install selenium")
    os.system("pip install selenium webdriver-manager")
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
'''install driver at first'''
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# ================= GLOBAL VARIABLES DEFINE =================
g_debug = 0
# ================= END GLOBAL VARIABLES =================


def threaded(func):
    def wraper(*args, **kwargs):
        thread = Thread(target=func, args=args, kwargs=kwargs)
        thread.start()

        return wraper


def debug__(frameinfo):
    print(f"{frameinfo.filename}:{frameinfo.lineno}")


def init_vars():

    pass

def find_contents(link,keysw,user=None,password=None):
    driver = webdriver.Edge()
    driver.get(link)
    time.sleep(1) # stay on the page within 2 sec
    if user!=None and password!=None:
        print("aaa")
        #  driver.find_element("id", "id_username").send_keys(user)
        #  driver.find_element("id", "id_password").send_keys(password+Keys.RETURN)
    # content = driver.find_element(by="id",value=keysw)
    print(driver.page_source)
    time.sleep(2) # stay on the page within 2 sec
    return
    # print(content.text)


logo = \
    R'''         _                                           
__      __  ___ | |__    ___   ___  _ __   __ _  _ __    ___ 
\ \ /\ / / / _ \| '_ \  / __| / __|| '__| / _` || '_ \  / _ \
 \ V  V / |  __/| |_) | \__ \| (__ | |   | (_| || |_) ||  __/
  \_/\_/   \___||_.__/  |___/ \___||_|    \__,_|| .__/  \___|
                                                |_|          
* author: laomi3u
* created: 29.04.2023                                                
'''
