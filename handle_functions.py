import os
import sys
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

def find_contents(link):
    driver = webdriver.Edge()
    driver.get('https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/')
    content = driver.find_element(by="id",value="page-heading")
    print(content.text)


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
