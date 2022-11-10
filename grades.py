import requests
import bs4 as BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
url = "https://hac.aldineisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fHomeAccess"

ser = Service("C:\Program Files (x86)\chromedriver.exe")

driver = webdriver.Chrome(service=ser)

driver.get(url)

time.sleep(10)

try:
    un = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "LogOnDetails_UserName")))
    un.send_keys("USERNAME")
    time.sleep(5)
except:
    print("Couldn't locate Username element.")
    driver.quit()

try:
    pwd = WebDriverWait(driver, 10).until(EC.presence_of_element_located(By.XPATH, "//input[@name='LogOnDetails.Password']"))
    pwd.send_keys("PASSWORD")
    time.sleep(5)

except:
    print("Couldn't locate Password element.")
    driver.quit()